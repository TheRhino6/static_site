import re

def extract_markdown_images(text):
    url = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    alt_text = re.findall(r"\[(.*?)\]", text)

    result = []
    for i in range (len(alt_text)):
        result.append((alt_text[i], url[i]))
    return url

def extract_markdown_links(text):
    url = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    link_text = re.findall(r"\[(.*?)\]", text)

    result = []
    for i in range (len(link_text)):
        result.append((link_text[i], url[i]))
    return url