from enum import Enum


# Define an enumeration for different types of text nodes
class TextType(Enum):
    PLAIN = "plain_text"
    BOLD = "bold_text"
    ITALIC = "italic_text"
    STRIKETHROUGH = "strikethrough_text"
    CODE = "code_text"
    LINK = "link_text"
    IMAGE = "image_text"


class TextNode:
    def __init__(
        self, text: str, text_type: TextType = TextType.PLAIN, url: str = None
    ):
        self.text = text
        self.text_type = text_type
        if url:
            self.url = url

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, TextNode):
            return False
        return (
            self.text == value.text
            and self.text_type == value.text_type
            and getattr(self, "url", None) == getattr(value, "url", None)
        )

    def __repr__(self) -> str:
        return f"TextNode(text={self.text!r}, text_type={self.text_type.value}, url={getattr(self, 'url', None)!r})"
