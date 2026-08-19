import re

def markdown_to_blocks(markdown):
    matches = markdown.split("\n\n")
    result = []
    for match in matches:
        a = match.strip()
        result.append(a.strip("\n"))
    return result