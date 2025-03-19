from textnode import TextNode


def main():
    sample_node = TextNode("Text for testing", "bold", "https://www.boot.dev")

    print(sample_node.__repr__())


if __name__ == "__main__":
    main()
