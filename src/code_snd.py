import re
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
        else:
            parts = old_node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError("Delimiter must be present in the text an odd number of times")
            for i in range(len(parts)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(parts[i], TextType.PLAIN))
                else:
                    new_nodes.append(TextNode(parts[i], text_type))
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
        else:
            matches = extract_markdown_images(old_node.text)
            if not matches:
                new_nodes.append(old_node)
            else:
                parts = re.split(r"!\[[^\[\]]*\]\([^\(\)]*\)", old_node.text)
                for i in range(len(parts)):
                    if parts[i]:
                        new_nodes.append(TextNode(parts[i], TextType.PLAIN))
                    if i < len(matches):
                        new_nodes.append(TextNode(matches[i][0], TextType.IMAGE, matches[i][1]))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
        else:
            matches = extract_markdown_links(old_node.text)
            if not matches:
                new_nodes.append(old_node)
            else:
                parts = re.split(r"(?<!!)\[[^\[\]]*\]\([^\(\)]*\)", old_node.text)
                for i in range(len(parts)):
                    if parts[i]:
                        new_nodes.append(TextNode(parts[i], TextType.PLAIN))
                    if i < len(matches):
                        new_nodes.append(TextNode(matches[i][0], TextType.LINK, matches[i][1]))
    return new_nodes