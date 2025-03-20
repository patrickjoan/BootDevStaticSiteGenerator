import unittest

from htmlnode import HTMLNode


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
        node = HTMLNode(props={"class": "container", "id": "main", "data-test": "value"})
        
        # Since dict order is not guaranteed, we need to check each attribute separately
        html = node.props_to_html()
        self.assertIn(' class="container"', html)
        self.assertIn(' id="main"', html)
        self.assertIn(' data-test="value"', html)
        
        # Check the length matches what we expect
        expected_length = len(' class="container"') + len(' id="main"') + len(' data-test="value"')
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


if __name__ == "__main__":
    unittest.main()
