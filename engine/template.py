import re
import os

#from tornado.ncss import ncssbook_log

TEMPLATE_PATH = "templates"

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

    def add_child(self, node):
        self.children.append(node)

    def render(self, context):
        result = ''
        for i in self.children:
            result += i.render(context)

        return result



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
        return self._parse_group()
    
    def _parse_group(self):
        root = GroupNode([])
        while not self.end():
            if self.peek().startswith('{{'):
                # eval node
                root.add_child(self._parse_eval())
            elif self.peek().startswith("{%"):
                # check tag type
                if self.peek().startswith("{% include "):
                    re_match = re.match(r'{%\s*include\s*"([\w.]+)"\s%}',self.next())
                    file_name = os.path.join(TEMPLATE_PATH, re_match.group(1))
                    root.add_child(Parser(tokenize(open(file_name).read())).parse())

            else:
                # text node
                root.add_child(self._parse_text())
        return root


    def _parse_text(self):
        return TextNode(self.next())

    def _parse_eval(self):
        return PythonNode(self.next().replace('{{', '').replace('}}', ''))

def render(filename, context):
    """
    render the file "filename" in templates using the dictionary "context"
    as global variables
    """
    text = open(os.path.join(TEMPLATE_PATH, filename)).read()
    tokens = tokenize(text)
    return Parser(tokens).parse().render(context)

if __name__ == "__main__":
    print(render("test.html", {'b': 'a'}))
