from enum import Enum
from node_markdown import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    LINE_CODE = "line_code"
    BLOCK_CODE = "block_code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
def text_node_to_html_node(text_node):
    t_type = text_node.text_type
    if t_type is TextType.TEXT:
        return LeafNode(None, text_node.text, None)
    elif t_type is TextType.BOLD:
        return LeafNode("b", text_node.text, None)
    elif t_type is TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif t_type is TextType.CODE:
        return LeafNode("code", text_node.text, None)
    elif t_type is TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif t_type is TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("improper text node type")

def text_node_to_markdown_node(text_node):
    t_type = text_node.text_type
    match t_type:
        case TextType.TEXT:
        case TextType.BOLD:
        case TextType.ITALIC:
        case TextType.CODE:
        case TextType.LINK:
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("improper text node type")

    if t_type is TextType.TEXT:
        return LeafNode(None, text_node.text, None)
    elif t_type is TextType.BOLD:
        return LeafNode("b", text_node.text, None)
    elif t_type is TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif t_type is TextType.CODE:
        return LeafNode("code", text_node.text, None)
    elif t_type is TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif t_type is TextType.IMAGE:
    else: