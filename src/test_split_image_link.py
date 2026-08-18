import unittest
from code_snd import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image(self):
        node = [
            TextNode("This is a plain text node with an ![image](https://i.imgur.com/zjjcJKZ.png) in it.", TextType.PLAIN),
        ]

        new_nodes = split_nodes_image(node)

        expected_nodes = [
            TextNode("This is a plain text node with an ", TextType.PLAIN),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" in it.", TextType.PLAIN),
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
            TextNode("This is text with an ", TextType.PLAIN),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.PLAIN),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
        new_nodes,
        )

    def test_split_nodes_image_no_images(self):
        node = [
            TextNode("This is a plain text node with no images.", TextType.PLAIN),
        ]

        new_nodes = split_nodes_image(node)

        expected_nodes = [
            TextNode("This is a plain text node with no images.", TextType.PLAIN),
        ]

        self.assertEqual(new_nodes, expected_nodes)

class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link(self):
        node = [
            TextNode("This is a plain text node with a [link](https://www.boot.dev) in it.", TextType.PLAIN),
        ]

        new_nodes = split_nodes_link(node)

        expected_nodes = [
            TextNode("This is a plain text node with a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://www.boot.dev"),
            TextNode(" in it.", TextType.PLAIN),
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.boot.dev) and another [second link](https://www.example.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and another ", TextType.PLAIN),
            TextNode("second link", TextType.LINK, "https://www.example.com"),
            ],
        new_nodes,
        )

    def test_split_nodes_link_no_links(self):
        node = [
            TextNode("This is a plain text node with no links.", TextType.PLAIN),
        ]

        new_nodes = split_nodes_link(node)

        expected_nodes = [
            TextNode("This is a plain text node with no links.", TextType.PLAIN),
        ]

        self.assertEqual(new_nodes, expected_nodes)