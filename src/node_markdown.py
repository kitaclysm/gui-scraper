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
            # case TextType.BLOCK_CODE:
            #     return f"```\n{self.value}\n```"
            case TextType.LINK:
                return f"[{self.value}]({self.link})"
            case TextType.IMAGE:
                return f"![{self.value}]({self.link})"

class ParentNode(MDNode):
    def __init__(self, kind, children, link):
        super().__init__(kind = kind, value = None, children = children, link = link)
    
    def to_markdown(self):
        if self.kind is None:
            raise ValueError("no tag")
        if self.children is None:
            raise ValueError("no children")
        match self.kind:
            case BlockType.HEADING1:
                content = "".join([child.to_markdown() for child in self.children])
                return f"# {content}\n\n"
            case BlockType.HEADING2:
                content = "".join([child.to_markdown() for child in self.children])
                return f"## {content}\n\n"
            case BlockType.HEADING3:
                content = "".join([child.to_markdown() for child in self.children])
                return f"### {content}\n\n"
            case BlockType.HEADING4:
                content = "".join([child.to_markdown() for child in self.children])
                return f"#### {content}\n\n"
            case BlockType.HEADING5:
                content = "".join([child.to_markdown() for child in self.children])
                return f"##### {content}\n\n"
            case BlockType.HEADING6:
                content = "".join([child.to_markdown() for child in self.children])
                return f"###### {content}\n\n"
            # case BlockType.LINE_CODE:
            #     content = "".join([child.to_markdown() for child in self.children])
            #     return f"`{content}`"
            case BlockType.BLOCK_CODE:
                content = "".join([child.to_markdown() for child in self.children])
                return f"```\n{content}\n```"
            case BlockType.QUOTE:
                content = ""
                for child in self.children:
                    content += f"> {child.to_markdown()}\n"
                return f"{content}\n"
            case BlockType.U_LIST:
                content = ""
                for child in self.children:
                    content += f"- {child.to_markdown()}\n"
                return f"{content}\n"
            case BlockType.O_LIST:
                content = ""
                for i in range(len(self.children)):
                    content += f"{i + 1}. {self.children[i].to_markdown()}\n"
                return f"{content}\n"
            case BlockType.PARAGRAPH:
                content = "".join([child.to_markdown() for child in self.children])
                return f"{content}\n\n"
            case _:
                raise Exception("invalid BlockType")