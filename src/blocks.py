from blocktype import *
from htmlnode import *
from text_to_textnode import *
from textnode import *

def markdown_to_blocks(markdown):
    matches = markdown.split("\n\n")
    result = []
    for match in matches:
        a = match.strip()
        if a != "":
            result.append(a.strip("\n"))
    return result

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            txt = block.replace("\n", " ")
            paragraph = ParentNode(tag="p", children=text_to_children(txt), props=None)
            children.append(paragraph)

        elif block_type == BlockType.HEADING:
            is_hash = True
            hash_count = 0
            while is_hash == True:
                if block[hash_count] == "#":
                    hash_count += 1
                else:
                    is_hash = False
            txt = block[hash_count:].strip()
            heading = ParentNode(tag=f"h{hash_count}", children=text_to_children(txt), props=None)
            children.append(heading)

        elif block_type == BlockType.CODE:
            txt = block_strip(block)
            text_node = TextNode(text=txt, text_type=TextType.CODE, url=None)
            child_node = text_node_to_html_node(text_node)
            code = ParentNode(tag="pre", children=[child_node], props=None)
            children.append(code)

        elif block_type == BlockType.QUOTE:
            txt = block.replace("> ", "")
            quote = ParentNode(tag="blockquote", children=text_to_children(txt), props=None)
            children.append(quote)

        elif block_type == BlockType.UNORDERED_LIST:
            split_txt = block.split("\n")
            txt = []
            for line in split_txt:
                clean_txt = line.replace("- ", "").strip()
                txt.append(ParentNode(tag="li", children=text_to_children(clean_txt), props=None))
            unordered = ParentNode(tag="ul", children=txt, props=None)
            children.append(unordered)

        elif block_type == BlockType.ORDERED_LIST:
            split_txt = block.split("\n")
            txt = []
            line_num = 1
            for line in split_txt:
                clean_txt = line.replace(f"{line_num}. ", "").strip()
                line_num += 1
                txt.append(ParentNode(tag="li", children=text_to_children(clean_txt), props=None))
            ordered = ParentNode(tag="ol", children=txt, props=None)
            children.append(ordered)

    return ParentNode(tag="div", children=children, props=None)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    result = []
    for node in text_nodes:
        result.append(text_node_to_html_node(node))
    return result

def block_strip(text):
    backtick = True
    i = 0
    while backtick == True:
        if text[i] == "`":
            i +=  1
        elif text[i] == "\n":
            i += 1
        else:
            backtick = False

    tick = True
    j = len(text) - 1
    while tick == True:
        if text[j] == "`":
            j -= 1
        else:
            tick = False

    a = text[i:]
    b = a[:j-i+1]
    return b