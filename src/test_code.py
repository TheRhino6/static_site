import unittest
from code_snd import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [
            TextNode("This is a plain text node with *bold* text.", TextType.PLAIN),
            TextNode("This is another plain text node.", TextType.PLAIN)
        ]
        delimiter = "*"
        text_type = TextType.BOLD

        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)

        expected_nodes = [
            TextNode("This is a plain text node with ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.PLAIN),
            TextNode("This is another plain text node.", TextType.PLAIN)
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_odd_occurrences(self):
        old_nodes = [
            TextNode("This is a plain text node with *bold* and *italic* text.", TextType.PLAIN)
        ]
        delimiter = "*"
        text_type_bold = TextType.BOLD
        text_type_italic = TextType.ITALIC

        new_nodes_bold = split_nodes_delimiter(old_nodes, delimiter, text_type_bold)
        new_nodes_italic = split_nodes_delimiter(old_nodes, delimiter, text_type_italic)

        expected_nodes_bold = [
            TextNode("This is a plain text node with ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.PLAIN),
            TextNode("italic", TextType.BOLD),
            TextNode(" text.", TextType.PLAIN)
        ]

        expected_nodes_italic = [
            TextNode("This is a plain text node with ", TextType.PLAIN),
            TextNode("bold", TextType.ITALIC),
            TextNode(" and ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.PLAIN)
        ]

        self.assertEqual(new_nodes_bold, expected_nodes_bold)
        self.assertEqual(new_nodes_italic, expected_nodes_italic)