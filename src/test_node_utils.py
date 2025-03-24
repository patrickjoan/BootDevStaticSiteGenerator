import unittest

from node_utils import text_node_to_html_node
from textnode import TextNode, TextType


class TestNodeUtils(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

    def test_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")
        self.assertEqual(html_node.to_html(), "<i>This is a italic node</i>")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
        self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(node)
        
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        
        self.assertEqual(html_node.props["href"], "https://www.example.com")
        
        expected_html = '<a href="https://www.example.com">This is a link node</a>'
        self.assertEqual(html_node.to_html(), expected_html)

    def test_image(self):
        node = TextNode("Alt text for image", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        
        self.assertEqual(html_node.props["src"], "https://example.com/image.png")
        self.assertEqual(html_node.props["alt"], "Alt text for image")
        
        expected_html = '<img src="https://example.com/image.png" alt="Alt text for image">'
        self.assertEqual(html_node.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()

