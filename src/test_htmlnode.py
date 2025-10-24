import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_init_all_params(self):
        node = HTMLNode(
            tag="p",
            value="This is a paragraph.",
            children=[HTMLNode(tag="b", value="bold")],
            props={"class": "text-center", "id": "main-paragraph"},
        )
        self.assertEqual(node._tag, "p")
        self.assertEqual(node._value, "This is a paragraph.")
        self.assertEqual(len(node._children), 1)
        self.assertEqual(node._children[0]._tag, "b")
        self.assertEqual(node._props, {"class": "text-center", "id": "main-paragraph"})

    def test_init_none_children_props(self):
        node = HTMLNode(tag="div", value="Hello", children=None, props=None)
        self.assertEqual(node._tag, "div")
        self.assertEqual(node._value, "Hello")
        self.assertEqual(node._children, [])
        self.assertEqual(node._props, {})

    def test_init_only_tag_value(self):
        node = HTMLNode(tag="span", value="Simple text", children=None, props=None)
        self.assertEqual(node._tag, "span")
        self.assertEqual(node._value, "Simple text")
        self.assertEqual(node._children, [])
        self.assertEqual(node._props, {})

    def test_to_html_not_implemented(self):
        node = HTMLNode(tag="p", value="test", children=None, props=None)
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html_single_prop(self):
        node = HTMLNode(
            tag="a", value="link", children=None, props={"href": "https://example.com"}
        )
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(
            tag="img",
            value=None,
            children=None,
            props={"src": "/image.png", "alt": "An image"},
        )
        # Order of properties in dict is not guaranteed in older Python versions,
        # so check for both possible orders if needed, or ensure stable order for comparison.
        # For modern Python (3.7+), dict insertion order is preserved.
        expected1 = ' src="/image.png" alt="An image"'
        expected2 = ' alt="An image" src="/image.png"'
        actual = node.props_to_html()
        self.assertIn(actual, [expected1, expected2])

    def test_props_to_html_empty_props(self):
        node = HTMLNode(tag="div", value="no props", children=None, props={})
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        child_node = HTMLNode(tag="b", value="bold", children=None, props=None)
        node = HTMLNode(
            tag="p", value="Hello", children=[child_node], props={"id": "greeting"}
        )
        expected_repr = "HTMLNode(tag='p', value='Hello', children=[HTMLNode(tag='b', value='bold', children=[], props={})], props={'id': 'greeting'})"
        self.assertEqual(repr(node), expected_repr)

    def test_repr_no_children_no_props(self):
        node = HTMLNode(tag="span", value="simple")
        expected_repr = "HTMLNode(tag='span', value='simple', children=[], props={})"
        self.assertEqual(repr(node), expected_repr)
