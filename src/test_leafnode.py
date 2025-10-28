import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_init_no_props(self):
        """Test LeafNode initialization without props."""
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node._tag, "p")
        self.assertEqual(node._value, "This is a paragraph.")
        self.assertDictEqual(node._props, {})

    def test_init_with_props(self):
        """Test LeafNode initialization with props."""
        props = {"href": "https://example.com", "target": "_blank"}
        node = LeafNode("a", "Click me", props)
        self.assertEqual(node._tag, "a")
        self.assertEqual(node._value, "Click me")
        # Ensure props are correctly stored (order doesn't matter for dict equality)
        self.assertEqual(node._props, props)

    def test_to_html_no_tag(self):
        """Test to_html when tag is None, should return just the value."""
        node = LeafNode(None, "Just plain text.")
        self.assertEqual(node.to_html(), "Just plain text.")

    def test_to_html_with_tag_no_props(self):
        """Test to_html with a tag and value, no props."""
        node = LeafNode("span", "Hello World")
        self.assertEqual(node.to_html(), "<span>Hello World</span>")

    def test_to_html_with_tag_and_props(self):
        """Test to_html with a tag, value, and props."""
        # For props, the order in props_to_html() might vary depending on dict iteration order
        # (though Python 3.7+ guarantees insertion order). For robustness, check both permutations.
        node = LeafNode("p", "Styled text", {"class": "bold", "id": "my-id"})
        expected_output1 = '<p class="bold" id="my-id">Styled text</p>'
        expected_output2 = '<p id="my-id" class="bold">Styled text</p>'
        actual_output = node.to_html()
        self.assertIn(
            actual_output,
            [expected_output1, expected_output2],
            f"Expected one of '{expected_output1}' or '{expected_output2}', but got '{actual_output}'",
        )

    def test_to_html_value_is_none_raises_error(self):
        """Test to_html raises ValueError if _value is None (though init type hints prevent this directly)."""
        # While __init__ requires `value: str`, `to_html` explicitly checks `if self._value is None: raise ValueError`.
        # We must manually set `_value = None` to test this specific branch.
        node = LeafNode("div", None)
        with self.assertRaisesRegex(
            ValueError, "LeafNode must have a value to convert to HTML"
        ):
            node.to_html()
