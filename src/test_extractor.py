from unittest import TestCase
from extractor import extract_markdown_images, extract_markdown_links


class TestExtractor(TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_multiple_images(self):
        """Test extracting multiple images from text."""
        matches = extract_markdown_images(
            "This is text with multiple images: ![first](https://example.com/img1.png) and ![second](https://example.com/img2.png)"
        )
        self.assertListEqual([
            ("first", "https://example.com/img1.png"),
            ("second", "https://example.com/img2.png")
        ], matches)

    def test_multiple_links(self):
        """Test extracting multiple links from text."""
        matches = extract_markdown_links(
            "This is text with [one link](https://example.com) and [another link](https://example.org)"
        )
        self.assertListEqual([
            ("one link", "https://example.com"),
            ("another link", "https://example.org")
        ], matches)

    def test_images_and_links_together(self):
        """Test that images don't get extracted as links."""
        text = "This has a ![image](https://example.com/img.png) and a [link](https://example.com)"
        image_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)
        
        self.assertListEqual([("image", "https://example.com/img.png")], image_matches)
        self.assertListEqual([("link", "https://example.com")], link_matches)

    def test_empty_text(self):
        """Test behavior with empty text."""
        self.assertListEqual([], extract_markdown_images(""))
        self.assertListEqual([], extract_markdown_links(""))

    def test_no_matches(self):
        """Test behavior with text that has no matches."""
        self.assertListEqual([], extract_markdown_images("This text has no images."))
        self.assertListEqual([], extract_markdown_links("This text has no links."))

    def test_complex_urls(self):
        """Test with URLs containing query parameters and fragments."""
        matches = extract_markdown_links(
            "Check out [this page](https://example.com/path?query=value&other=123#fragment)"
        )
        self.assertListEqual([
            ("this page", "https://example.com/path?query=value&other=123#fragment")
        ], matches)

    def test_empty_alt_text(self):
        """Test images with empty alt text."""
        matches = extract_markdown_images("This has an empty alt text image: ![](https://example.com/img.png)")
        self.assertListEqual([("", "https://example.com/img.png")], matches)

    def test_empty_anchor_text(self):
        """Test links with empty anchor text."""
        matches = extract_markdown_links("This has an empty anchor text link: [](https://example.com)")
        self.assertListEqual([("", "https://example.com")], matches)

    def test_nested_brackets(self):
        """Test that the regex handles nested brackets correctly."""
        # This should not be a valid match in either function
        text = "This has nested brackets: [text with [nested] brackets](https://example.com)"
        image_matches = extract_markdown_images(text.replace("[", "!["))
        link_matches = extract_markdown_links(text)
        
        self.assertListEqual([], image_matches)
        self.assertListEqual([], link_matches)

    def test_malformed_markdown(self):
        """Test with malformed markdown syntax."""
        # Missing closing bracket
        text1 = "This is malformed: [link(https://example.com)"
        # Missing closing parenthesis
        text2 = "This is malformed: [link](https://example.com"
        
        self.assertListEqual([], extract_markdown_links(text1))
        self.assertListEqual([], extract_markdown_links(text2))
