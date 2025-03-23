import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_init_default_values(self):
        # Test initialization with default values
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

        # Test that default collections are different objects
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertIsNot(node1.children, node2.children)
        self.assertIsNot(node1.props, node2.props)

    def test_init_with_values(self):
        # Test initialization with specific values
        children = [HTMLNode(), HTMLNode()]
        props = {"class": "container", "id": "main"}

        node = HTMLNode("div", "content", children, props)

        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "content")
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, props)

    def test_props_to_html_empty(self):
        # Test with empty props
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

        # Test with None props (should be converted to empty dict)
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_props(self):
        # Test with single prop
        node = HTMLNode(props={"class": "container"})
        self.assertEqual(node.props_to_html(), ' class="container"')

        # Test with multiple props
        node = HTMLNode(
            props={"class": "container", "id": "main", "data-test": "value"}
        )

        # Since dict order is not guaranteed, we need to check each attribute separately
        html = node.props_to_html()
        self.assertIn(' class="container"', html)
        self.assertIn(' id="main"', html)
        self.assertIn(' data-test="value"', html)

        # Check the length matches what we expect
        expected_length = (
            len(' class="container"') + len(' id="main"') + len(' data-test="value"')
        )
        self.assertEqual(len(html), expected_length)

    def test_to_html_raises_not_implemented(self):
        # Test that to_html raises NotImplementedError
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr(self):
        # Test the string representation
        node = HTMLNode("div", "content", [HTMLNode()], {"class": "container"})
        repr_str = repr(node)

        # Check that it contains the key components
        self.assertIn("tag='div'", repr_str)
        self.assertIn("value='content'", repr_str)
        self.assertIn("children=", repr_str)
        self.assertIn("props={'class': 'container'}", repr_str)


class TestLeafNode(unittest.TestCase):
    def test_leaf_node_initialization(self):
        # Test basic initialization
        node = LeafNode("Hello", "p")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

        # Test with props
        node = LeafNode("Hello", "p", {"class": "greeting"})
        self.assertEqual(node.props, {"class": "greeting"})

    def test_leaf_node_requires_value(self):
        # Test that value is required
        with self.assertRaises(ValueError):
            LeafNode(None, "p")

    def test_leaf_to_html_with_tag(self):
        # Test rendering with a tag
        node = LeafNode("Hello, world!", "p")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        # Test with different tag types
        node = LeafNode("Hello, world!", "h1")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

        node = LeafNode("Click me!", "a", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_without_tag(self):
        # Test rendering without a tag
        node = LeafNode("Raw text", None)
        self.assertEqual(node.to_html(), "Raw text")

    def test_leaf_to_html_empty_value(self):
        # Test that empty value raises an error
        node = LeafNode("", "p")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_repr(self):
        # Test the string representation
        node = LeafNode("Hello", "p", {"class": "greeting"})
        repr_str = repr(node)

        # Verify it includes all important parts
        self.assertIn("tag='p'", repr_str)
        self.assertIn("value='Hello'", repr_str)
        self.assertIn("props={'class': 'greeting'}", repr_str)


if __name__ == "__main__":
    unittest.main()
