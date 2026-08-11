import unittest
from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HtmlNode("<p>This is a paragraph</p>")
        node2 = HtmlNode("<p>This is a paragraph</p>")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HtmlNode("<p>This is a paragraph</p>")
        node2 = HtmlNode("<div>This is a div</div>")
        self.assertNotEqual(node, node2)

    def test_eq_different_type(self):
        node = HtmlNode("<p>This is a paragraph</p>")
        self.assertNotEqual(node, "This is a string")