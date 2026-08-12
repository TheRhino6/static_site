import unittest
from htmlnode import HtmlNode, LeafNode, ParentNode
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

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

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

class TestParentNode(unittest.TestCase):
    def test_parent_to_html_div(self):
        child1 = LeafNode("p", "Hello, world!")
        child2 = LeafNode("p", "This is a test.")
        parent_node = ParentNode("div", children=[child1, child2])
        self.assertEqual(parent_node.to_html(), "<div><p>Hello, world!</p><p>This is a test.</p></div>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>", "ParentNode with grandchildren should render correctly")