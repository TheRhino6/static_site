from textnode import TextNode, TextType
from code_snd import *

def text_to_textnodes(text):
    return split_nodes_link(
        split_nodes_image(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        [TextNode(text, TextType.PLAIN)], "**", TextType.BOLD), "_", TextType.ITALIC), "`", TextType.CODE)))

