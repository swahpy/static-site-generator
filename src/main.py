from textnode import TextNode, TextType


def main():
    node = TextNode("Hello, world!", TextType.BOLD_TEXT)
    print(node)


if __name__ == "__main__":
    main()
