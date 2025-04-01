VOID_ELEMENTS = {"img", "input", "br", "hr", "meta", "link", "area", "base", "col", "embed", "source", "track", "wbr"}

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        output_html = ""
        for key in self.props:
            output_html += f' {key}="{self.props[key]}"'
        return output_html

    def __repr__(self) -> str:
        return f"HTMLNode(tag={repr(self.tag)}, value={repr(self.value)}, children={repr(self.children)}, props={repr(self.props)})"


class LeafNode(HTMLNode):
    def __init__(self, value, tag, props=None) -> None:
        if value is None:
            raise ValueError("Value is required for LeafNode")
        super().__init__(tag, value, [], props)
        

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        if self.tag is None:
            return self.value
        
        # Special case for void elements like img
        props_html = self.props_to_html()
        if self.tag in VOID_ELEMENTS:
            return f"<{self.tag}{props_html}>"
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode(tag={repr(self.tag)}, value={repr(self.value)}, props={repr(self.props)})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        if tag is None:
            raise ValueError("Tag is required for ParentNode")

        super().__init__(tag, None, children, props)


    def to_html(self) -> str:
        if not self.children:
            raise ValueError("No children for ParentNode")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode(tag={repr(self.tag)}, children={repr(self.children)}, props={repr(self.props)})"
