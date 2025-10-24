from __future__ import annotations


class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list["HTMLNode"] = None,
        props: dict[str, str] = None,
    ) -> None:
        """
        Initializes an HTMLNode object.

        Args:
            tag (str, optional): The HTML tag name (e.g., 'p', 'div'). Defaults to None.
            value (str, optional): The text content of the node. Defaults to None.
            children (list[HTMLNode], optional): A list of child HTMLNode objects.
                                                  Defaults to an empty list.
            props (dict[str, str], optional): A dictionary of HTML attributes.
                                               Defaults to an empty dictionary.
        """
        self._tag = tag
        self._value = value
        self._children = children if children is not None else []
        self._props = props if props is not None else {}

    def to_html(self) -> str:
        """
        Converts the HTMLNode and its children into an HTML string.
        This method must be implemented by subclasses, as the base HTMLNode
        does not specify how to render itself.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Subclasses must implement to_html method")

    def props_to_html(self) -> str:
        """
        Converts the `_props` dictionary into a space-separated string of HTML attributes.

        Returns:
            str: A string of HTML attributes (e.g., ' key="value"').
            Returns an empty string if `_props` is empty.
        """
        result = " ".join(f'{key}="{value}"' for key, value in self._props.items())
        return f" {result}" if result else ""

    def __repr__(self) -> str:
        """Returns a string representation of the HTMLNode for debugging."""
        return f"HTMLNode(tag={self._tag!r}, value={self._value!r}, children={self._children!r}, props={self._props!r})"
