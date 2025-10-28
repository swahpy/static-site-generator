from typing import override

from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] = None) -> None:
        super().__init__(tag, value, props=props)

    @override
    def to_html(self) -> str:
        if self._value is None:
            raise ValueError("LeafNode must have a value to convert to HTML")
        if self._tag is None:
            return self._value
        return f"<{self._tag}{self.props_to_html()}>{self._value}</{self._tag}>"
