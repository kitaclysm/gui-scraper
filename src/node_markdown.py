class MDNode():
    # kind: type of text
    # value: visible text
    # children: nested MD nodes
    # link: destination URL for links and images
    def __init__(self, kind=None, value=None, children=None, link=None):
        self.kind = kind
        self.value = value
        self.children = children
        self.link = link

    def to_markdown(self):
        raise NotImplementedError()

    def __repr__(self):
        return f"Kind: {self.kind}, Value: {self.value}, Children: {self.children}, Link: {self.link}"

class LeafNode(MDNode):
    def __init__(self, kind, value, link):
        super().__init__(kind = kind, value = value, children = None, link = link)

    # this translates chunks of text into relevant MarkDown elements
    def to_markdown(self):
        if self.value is None:
            raise ValueError("no value")
        if self.kind is None:
            return self.value
        match self.kind:
            case TextType.TEXT:
                return self.value
            case TextType.BOLD:
                return f"**{self.value}**"
            case TextType.ITALIC:
                return f"*{self.value}*"
            case TextType.LINE_CODE:
                return f"`{self.value}`"
            case TextType.BLOCK_CODE:
                return f"```\n{self.value}\n```"
            case TextType.LINK:
                return f"[{self.value}]({self.link})"
            case TextType.IMAGE:
                return f"![{self.value}]({self.link})"

class ParentNode(MDNode):
    def __init__(self, kind, value, children, link):
        super().__init__(kind = kind, value = value, children = children, link = link)
    
    def to_markdown(self):
        if self.kind is None:
            raise ValueError("no tag")
        if self.children is None:
            raise ValueError("no children")
        children_string = ""
        for child in self.children:
            children_string += child.to_markdown()

def match_kind(node):
    match node.kind:
        case TextType.TEXT:
            return self.value
        case TextType.BOLD:
            return f"**{self.value}**"
        case TextType.ITALIC:
            return f"*{self.value}*"
        case TextType.LINE_CODE:
            return f"`{self.value}`"
        case TextType.BLOCK_CODE:
            return f"```\n{self.value}\n```"
        case TextType.LINK:
            return f"[{self.value}]({self.link})"
        case TextType.IMAGE:
            return f"![{self.value}]({self.link})"