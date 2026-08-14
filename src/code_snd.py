from textnode import TextNode, TextType

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