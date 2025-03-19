from textnode import TextNode, TextType


def main():
    sample_node = TextNode("Text for testing", TextType.LINK, "https://www.boot.dev")

    print(sample_node.__repr__())


if __name__ == "__main__":
    main()
