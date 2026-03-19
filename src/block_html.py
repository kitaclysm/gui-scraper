from enum import Enum
from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import LeafNode, ParentNode, HTMLNode
from inline_markdown import markdown_to_blocks, text_to_textnodes
import re

class BlockType(Enum):
    HEADING1 = "heading1"
    HEADING2 = "heading2"
    HEADING3 = "heading3"
    HEADING4 = "heading4"
    HEADING5 = "heading5"
    HEADING6 = "heading6"
    # LINE_CODE = "line_code"
    BLOCK_CODE = "block_code"
    QUOTE = "quote"
    U_LIST = "unordered_list"
    O_LIST = "ordered_list"
    PARAGRAPH = "paragraph"

def block_to_block_type(html):
    # split into parents
    # headings
    if html.startswith("<h"):
        if html.startswith("<h1"):
            return BlockType.HEADING1
        if html.startswith("<h2"):
            return BlockType.HEADING2    
        if html.startswith("<h3"):
            return BlockType.HEADING3    
        if html.startswith("<h4"):
            return BlockType.HEADING4    
        if html.startswith("<h5"):
            return BlockType.HEADING5    
        if html.startswith("<h6"):
            return BlockType.HEADING6
    
    # inline code
    if html.startswith("<code"):
        return BlockType.LINE_CODE
    
    # block code
    if html.startswith("<pre><code"):
        return BlockType.BLOCK_CODE

    # quote
    if html.startswith("<blockquote"):
        return BlockType.QUOTE
    
    # unordered list
    if html.startswith("<ul"):
        return BlockType.U_LIST
    
    # ordered list
    if html.startswith("<ol"):
        return BlockType.O_LIST

    # paragraph
    if html.startswith("<p"):
        return BlockType.PARAGRAPH