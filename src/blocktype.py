from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    # heading checker
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
        
    # code checker
    if block[0:4] == "```\n" and block[-3:len(block)] == "```":
        return BlockType.CODE

    # quote checker
    if block[0] == ">":
        quote = True
        for i in range(len(block)):
            if block[i] == "\n":
                if block[i+1] != ">":
                    quote = False
        if quote == True:
            return BlockType.QUOTE

    # unordered list checher
    if block[0:2] == "- ":
        unorder = True
        for i in range(len(block)):
            if block[i] == "\n":
                if block[i+1:i+3] != "- ":
                    unorder = False
        if unorder == True:
            return BlockType.UNORDERED_LIST

    # ordered list checker
    if block[0:3] == "1. ":
        ordered = True
        count = 1
        for i in range(len(block)):
            if block[i] == "\n":
                count += 1
                if block[i+1:i+4] != f"{count}. ":
                    ordered = False
        if ordered == True:
            return BlockType.ORDERED_LIST

    # paragraph return
    return BlockType.PARAGRAPH