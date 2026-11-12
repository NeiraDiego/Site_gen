class HTMLNode:
    def __init__(self, tag: str|None=None, value: str|None=None, children: list|None=None, props: dict|None=None):
        self.tag = tag #A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value #string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children #list of HTMLNode objects representing the children of this node
        self.props = props #dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    def to_html(self):
        return f"NotImplementedError"

    def props_to_html(self):
        if self.props == None or not self.props:
            return ""
        str_to_return = ""
        for element in self.props:
            str_to_return+= ' '+element+'='+self.props[element] 
        return str_to_return

    def __repr__(self):
        return f"""HTML Node:
        Tag = {self.tag}
        Value = {self.value}
        Children = {self.children}
        Props = {self.props_to_html}"""

    def __eq__(self, other) -> bool:
        if not isinstance(other, HTMLNode):
            return False
        return (
        self.tag == other.tag and
        self.value == other.value and
        self.children == other.children and 
        self.props == other.props)
