import os
from blocks import *

def extract_title(markdown):
    content = markdown.split("\n")
    for line in content:
        if line.startswith("# "):
            a = line[1:]
            return a.strip()
    raise Exception("No header found")

def generate_page(from_path, template_path, dest_path):
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        host = f.read()
    with open(template_path) as f:
        template = f.read()
    html = markdown_to_html_node(host).to_html()
    title = extract_title(host)
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, mode="w") as f:
        f.write(page)