import re
import os
import functools
import html

#from tornado.ncss import ncssbook_log

CRASH_ON_ERROR = False
TEMPLATE_PATH = "templates"
FOR_REGEX = r'{%\s*for\s+([\w]+)\s+in\s+(.+)\s*%}'

def escape(fn):
    @functools.wraps(fn)
    def magic(*args, **kwargs):
        return html.escape(fn(*args, **kwargs))
    return magic

class Node:
    """ node base class """
    def __init__(self):
        pass

    def render(self, context):
        raise NotImplementedError()

class TextNode(Node):
    """ contains html and other non python stuff """
    def __init__(self,content):
        self.content = content

    def render(self, context):
        return self.content

class PythonNode(Node):
    """ contain python code """
    def __init__(self,content):
        self.content = content

    @escape
    def render(self, context):
        try:
            return str(eval(self.content, {}, context))
        except Exception as e:
            if CRASH_ON_ERROR:
                raise TemplateRenderError(e)
            else:
                return "<strong>Error while evaluating python code {}: {}</strong>".format(self.content, e)

class GroupNode(Node):
    """ contains multiple nodes"""
    def __init__(self, children):
        self.children = children

    def add_child(self, nodes):
        for node in nodes:
            self.children.append(node)

    def render(self, context):
        result = ''
        for i in self.children:
            result += i.render(context)

        return result

class IfNode(GroupNode):
    def __init__(self, condition):
        super().__init__([])
        self.condition = condition

    def render(self, context):
        try:
            if eval(self.condition, {}, context):
                return super().render(context)
        except Exception as e:
            return "<strong>Error while evaluating if/elif/else condition '{}' - {}</strong>".format(self.condition, e)
        return ""

class ForNode(GroupNode):
    def __init__(self, forIterator, forList):
        super().__init__([])

        self._forIterator = forIterator
        self._forList = forList

    def render(self, context):
        context[self._forIterator] = 0
        result = ""
        for context[self._forIterator] in eval(self._forList):
            result += super().render(context)
        return result

class SafeNode(Node):
    def __init__(self, expr):
        self.expr = expr

    def render(self, context):
        try:
            return str(eval(self.expr, {}, context))
        except Exception as e:
            if CRASH_ON_ERROR:
                raise TemplateRenderError(e)
            else:
                return "<strong>Error while safe-evaluating python code {}: {}</strong>".format(self.expr, e)


class TemplateSyntaxError(Exception):
    pass

class TemplateRenderError(Exception):
    pass

def tokenize(text):
    """
    takes text and seperates into chunks for parsing

    >>> tokenize("{{ include test.html }} blah {% if yes %}")
    ['{{ include test.html }}', ' blah ', '{% if yes %}']
    """
    tokens = re.split(r'({%.*?%})|({{.*?}})', text)

    tokens = [x for x in tokens if x]

    return tokens

RE_IF = re.compile(r'{%\s*if\s*(.+?)\s*%}')
RE_ELSE = re.compile(r'{%\s*else\s*%}')
RE_INCLUDE = re.compile(r'{%\s*include\s*"([\w.]+)"\s%}')


class Parser:
    """ parsers tokens into a parse tree to be rendered """
    def __init__(self, tokens):
        self._tokens = tokens
        self._position = 0

    def end(self):
        return self._position == len(self._tokens)

    def peek(self):
        if not self.end():
            return self._tokens[self._position]
        return None

    def next(self):
        self._position += 1
        return self._tokens[self._position-1]

    def parse(self):
        return self._parse_group(True)

    def _parse_group(self, is_root=False, root=None):

        elses = []

        if not root:
            root = GroupNode([])

        while not self.end(): # TODO explode if is_root and we see an end if or something
            if self.peek().startswith('{{'):
                # eval node
                root.add_child(self._parse_eval())
            elif self.peek().startswith("{%"):
                # check tag type
                if self.peek().startswith("{% include "):
                    re_match = re.match(r'{%\s*include\s*"([\w.]+)"\s%}',self.next())
                    file_name = os.path.join(TEMPLATE_PATH, re_match.group(1))
                    try:
                        root.add_child(Parser(tokenize(open(file_name).read())).parse())
                    except Exception as e:
                        if CRASH_ON_ERROR:
                            raise e
                        else:
                            root.add_child([TextNode("<strong>Error while including file {}: {}</strong>".format(file_name, e))])
                elif self.peek().startswith("{% for"):
                    root.add_child(self._parse_for())
                elif self.peek().startswith("{% if "):
                    root.add_child(self._parse_if())
                elif self.peek().startswith("{% elif "):
                    if type(root) == IfNode:
                        return [root] + self._parse_elif()
                    else:
                        if CRASH_ON_ERROR:
                            raise TemplateSyntaxError("elif without an if")
                        else:
                            root.add_child([TextNode("<strong>elif '%s' has no matching if statement</strong>".format(self.peek()))])
                            self.next()
                elif self.peek().startswith("{% else"):
                    if type(root) == IfNode:
                        self.next()
                        condition = "not (" + root.condition +" )"
                        node = IfNode(condition)
                        elses += (self._parse_group(root=node))
                        return [root] + elses
                    else:
                        if CRASH_ON_ERROR:
                            raise TemplateSyntaxError("else without an if")
                        else:
                            root.add_child([TextNode("<strong>else has no matching if statement</strong>")])
                            self.next()

                elif self.peek().startswith("{% end "):
                    if is_root:
                        if CRASH_ON_ERROR:
                            raise TemplateSyntaxError("{} does not have a corresponding beginning statement".format(self.next()))
                        else:
                            root.add_child([TextNode("<strong>'{}' has no matching 'for' or 'if' statement</strong>".format(self.peek()))])
                            self.next()
                    else:
                        self.next()
                        if type(root) == IfNode:
                            return [root] + elses
                        return [root]
                elif self.peek().startswith("{% safe "):
                    root.add_child(self._parse_safe())
                else:
                    if CRASH_ON_ERROR:
                        raise TemplateSyntaxError("invalid {% ... %} statement: {}".format(self.next()))
                    else:
                        root.add_child([TextNode("<strong>WARNING: Invalid instruction - {}</strong>".format(self.next()))])
            else:
                # text node
                root.add_child(self._parse_text())
        if not is_root:
            # should never get here - we should have seen an
            # 'end x' statement
            if CRASH_ON_ERROR:
                raise TemplateSyntaxError("unmatched for or if")
            else:
                msg = "<strong>unmatched {} (looks like \"{}\") - need an 'end {}'"
                if type(root) == IfNode:
                    msg = msg.format("if/elif/else", "if {}".format(root.condition), "if")
                else:
                    msg = msg.format("for", "for {} in {}".format(root._forIterator, root._forList), "for")

                root.add_child([TextNode(msg)])
                z = root.children
                root.children = []
                return [root] + z
        return [root]

    def _parse_for(self):
        re_match = re.match(FOR_REGEX, self.next())

        forIterator = re_match.group(1).strip()
        forList = re_match.group(2).strip()
        forNode = ForNode(forIterator, forList)

        return self._parse_group(root=forNode)

    def _parse_if(self):
        match = re.match(r'{%\s*if\s*(.+?)\s*%}',self.next())
        condition = match.group(1)
        node = IfNode(condition)
        return self._parse_group(root=node)

    def _parse_elif(self):
        match = re.match(r'{%\s*elif\s*(.+?)\s*%}',self.next())
        condition = match.group(1)
        node = IfNode(condition)
        return self._parse_group(root=node)



    def _parse_text(self):
        return [TextNode(self.next())]

    def _parse_safe(self):
        return [SafeNode(self.next().replace('{%', '').replace('%}', '').strip()[4:])]

    def _parse_eval(self):
        return [PythonNode(self.next().replace('{{', '').replace('}}', ''))]

def render(filename, context):
    """
    render the file "filename" in templates using the dictionary "context"
    as global variables
    """
    text = open(os.path.join(TEMPLATE_PATH, filename)).read()
    tokens = tokenize(text)
    return Parser(tokens).parse()[0].render(context)

if __name__ == "__main__":
    print(render("test.html", {'a': 'B', 'b': 'a'}))
