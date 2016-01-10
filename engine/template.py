import re
import os

#from tornado.ncss import ncssbook_log

CRASH_ON_ERROR = False
TEMPLATE_PATH = "templates"
FOR_REGEX = r'{%\s*for\s+([\w]+)\s+in\s+(.+)\s*%}'

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

    def render(self, context):
        return str(eval(self.content, {}, context))

class GroupNode(Node):
    """ contains multiple nodes"""
    def __init__(self, children):
        self.children = children

    def add_child(self, nodes):
        for node in nodes:
            self.children.append(node)

    def render(self, context):
        result = ''
        print(self.children)
        for i in self.children:
            result += i.render(context)

        return result

class IfNode(GroupNode):
    def __init__(self, condition):
        super().__init__([])
        self.condition = condition

    def render(self, context):
        if eval(self.condition, {}, context):
            return super().render(context)
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
    #print(tokens)

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
                    root.add_child(Parser(tokenize(open(file_name).read())).parse())
                elif self.peek().startswith("{% for"):
                    root.add_child(self._parse_for())
                elif self.peek().startswith("{% if "):
                    root.add_child(self._parse_if())
                elif self.peek().startswith("{% elif "):
                    if type(root) == IfNode:
                        return [root] + self._parse_elif()
                    else:
                        raise TemplateSyntaxError("elif without an if")
                elif self.peek().startswith("{% else"):
                    if type(root) == IfNode:
                        self.next()
                        condition = "not (" + root.condition +" )"
                        node = IfNode(condition)
                        elses += (self._parse_group(root=node))
                        return [root] + elses
                        

                elif self.peek().startswith("{% end "):
                    if is_root:
                        raise TemplateSyntaxError("%s does not have a corresponding beginning statement"%(self.next()))
                    else:
                        self.next()
                        if type(root) == IfNode:
                            return [root] + elses
                        return [root]
                else:
                    raise Exception("lrn2code")
            else:
                # text node
                root.add_child(self._parse_text())
        if not is_root:
            # should never get here - we should have seen an
            # 'end x' statement
            raise TemplateSyntaxError("unmatched for or if")
        return [root]

    def _parse_for(self):
        re_match = re.match(FOR_REGEX, self.next())
        
        forIterator = re_match.group(1).strip()
        forList = re_match.group(2).strip()
        forNode = ForNode(forIterator, forList)

        print("\"" + forIterator + "\"\t\"" + forList + "\"")

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
