def test_bold_text_type(self):
    old_nodes = [TextNode("hello,world", "bold")]
    result = split_nodes_delimiter(old_nodes, ",", "bold")
    expected = [TextNode("hello", "bold"), TextNode("world", "bold")]
    self.assertEqual(result, expected)

def test_italic_text_type(self):
    old_nodes = [TextNode("hello,world", "italic")]
    result = split_nodes_delimiter(old_nodes, ",", "italic")
    expected = [TextNode("hello", "italic"), TextNode("world", "italic")]
    self.assertEqual(result, expected)

def test_code_text_type(self):
    old_nodes = [TextNode("hello,world", "code")]
    result = split_nodes_delimiter(old_nodes, ",", "code")
    expected = [TextNode("hello", "code"), TextNode("world", "code")]
    self.assertEqual(result, expected)

def test_multiple_consecutive_delimiters(self):
    old_nodes = [TextNode("hello,,world", "text")]
    result = split_nodes_delimiter(old_nodes, ",", "text")
    expected = [TextNode("hello", "text"), TextNode("", "text"), TextNode("world", "text")]
    self.assertEqual(result, expected)

def test_delimiter_at_boundaries(self):
    old_nodes = [TextNode(",hello,world,", "text")]
    result = split_nodes_delimiter(old_nodes, ",", "text")
    expected = [TextNode("", "text"), TextNode("hello", "text"), 
                TextNode("world", "text"), TextNode("", "text")]
    self.assertEqual(result, expected)

def test_different_delimiter(self):
    old_nodes = [TextNode("hello*world", "text")]
    result = split_nodes_delimiter(old_nodes, "*", "text")
    expected = [TextNode("hello", "text"), TextNode("world", "text")]
    self.assertEqual(result, expected)

    def test_multiple_nodes(self):
        old_nodes = [
            TextNode("hello,world", "text"),
            TextNode("foo", "text"),
            TextNode("bar,baz", "text"),
        ]
        result = split_nodes_delimiter(old_nodes, ",", "text")
        expected = [
            TextNode("hello", "text"),
            TextNode("world", "text"),
            TextNode("foo", "text"),
            TextNode("bar", "text"),
            TextNode("baz", "text"),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
