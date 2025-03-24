from htmlnode import LeafNode
from textnode import TextNode, TextType


def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise TypeError("Expected a TextNode object")

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(text_node.text, None)

        case TextType.BOLD:
            return LeafNode(text_node.text, "b")

        case TextType.ITALIC:
            return LeafNode(text_node.text, "i")

        case TextType.CODE:
            return LeafNode(text_node.text, "code")

        case TextType.LINK:
            if text_node.url is None:
                raise ValueError("URL is required for LINK text type")
            return LeafNode(text_node.text, "a", {"href": text_node.url})

        case TextType.IMAGE:
            if not text_node.url:
                raise ValueError("URL is required for IMAGE text type")
            return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})

        case _:
            raise ValueError(f"Unsupported TextType: {text_node.text_type}")
