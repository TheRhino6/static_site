import unittest
from text_to_textnode import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextnodes(unittest.TestCase):
    def test_basic(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        test = text_to_textnodes(text)

        expected_nodes = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.PLAIN),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(test, expected_nodes)

    def test_again(self):
        text = "Here is some **MORE** _italic text_ with a `code blocking the way` but the ![image of Yoda](https://i.imgur.com/fJRm4Vk.jpeg) will save the day with this [link](https://boot.dev)"

        test = text_to_textnodes(text)

        expected_nodes = [
            TextNode("Here is some ", TextType.PLAIN),
            TextNode("MORE", TextType.BOLD),
            TextNode(" ", TextType.PLAIN),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" with a ", TextType.PLAIN),
            TextNode("code blocking the way", TextType.CODE),
            TextNode(" but the ", TextType.PLAIN),
            TextNode("image of Yoda", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" will save the day with this ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(test, expected_nodes)