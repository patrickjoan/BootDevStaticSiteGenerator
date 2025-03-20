import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_initialization(self):
        # Test basic initialization
        node = TextNode("Hello", TextType.TEXT)
        self.assertEqual(node.text, "Hello")
        self.assertEqual(node.text_type, TextType.TEXT)
        self.assertIsNone(node.url)

        # Test with URL
        node_with_url = TextNode("Click here", TextType.LINK, "https://example.com")
        self.assertEqual(node_with_url.url, "https://example.com")

    def test_eq_identical_nodes(self):
        # Test equality with identical nodes
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

        # With URLs
        node3 = TextNode("Link", TextType.LINK, "https://boot.dev")
        node4 = TextNode("Link", TextType.LINK, "https://boot.dev")
        self.assertEqual(node3, node4)

    def test_eq_different_nodes(self):
        # Test with different text
        node1 = TextNode("Node 1", TextType.TEXT)
        node2 = TextNode("Node 2", TextType.TEXT)
        self.assertNotEqual(node1, node2)

        # Test with different text_type
        node3 = TextNode("Same text", TextType.BOLD)
        node4 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node3, node4)

        # Test with different URL
        node5 = TextNode("Link", TextType.LINK, "https://example.com")
        node6 = TextNode("Link", TextType.LINK, "https://different.com")
        self.assertNotEqual(node5, node6)

        # Test with one URL None
        node7 = TextNode("Link", TextType.LINK, "https://example.com")
        node8 = TextNode("Link", TextType.LINK)
        self.assertNotEqual(node7, node8)

    def test_eq_different_types(self):
        # Test equality with non-TextNode objects
        node = TextNode("Text", TextType.TEXT)
        self.assertNotEqual(node, "Text")
        self.assertNotEqual(node, 123)
        self.assertNotEqual(node, None)



    def test_repr(self):
        node = TextNode("Hello", TextType.TEXT)
        repr_str = repr(node)
        # Check individual components
        self.assertIn("'Hello'", repr_str)
        self.assertIn(str(TextType.TEXT), repr_str)
        self.assertIn("None", repr_str)



if __name__ == "__main__":
    unittest.main()
