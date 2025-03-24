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
    def __init__(self, value, tag=None, props=None) -> None:
        super().__init__(tag, value, [], props)

        if value is None:
            raise ValueError("Value is required for LeafNode")

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        if not self.tag:
            return str(self.value)

        props_html = self.props_to_html()
        
        # Special case for void elements like img
        if self.tag == "img":
            return f"<{self.tag}{props_html}>"
        
        # Normal case for regular elements
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode(tag={repr(self.tag)}, value={repr(self.value)}, props={repr(self.props)})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        if tag is None:
            raise ValueError("Tag is required for ParentNode")

        super().__init__(tag, None, children, props)


    def to_html(self):
        if not self.children:
            raise ValueError("No children for ParentNode")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode(tag={repr(self.tag)}, children={repr(self.children)}, props={repr(self.props)})"
