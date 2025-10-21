from enum import Enum


# Define an enumeration for different types of text nodes
class TextType(Enum):
    PLAIN_TEXT = "plain_text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    STRIKETHROUGH_TEXT = "strikethrough_text"
    CODE_TEXT = "code_text"
    LINK_TEXT = "link_text"
    IMAGE_TEXT = "image_text"


class TextNode:
    def __init__(
        self, text: str, text_type: TextType = TextType.PLAIN_TEXT, url: str = None
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
