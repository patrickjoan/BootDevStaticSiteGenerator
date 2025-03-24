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
        pass

    def test_italic(self):
        pass

    def test_code(self):
        pass

    def test_link(self):
        pass

    def test_image(self):
        pass


if __name__ == "__main__":
    unittest.main()

