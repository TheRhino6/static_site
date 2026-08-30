import os
from blocks import *
from copy_files import test_file_path_exists

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
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, mode="w") as f:
        f.write(page)

def generate_recursive(host, template, target):
    for item in os.listdir(host):
        item_path = os.path.join(host, item)
        if os.path.isfile(item_path) == True:
            dest_path = os.path.join(target, "index.html")
            generate_page(item_path, template, dest_path)
        elif os.path.isdir(item_path) == True:
            dest_path = os.path.join(target, item)
            if test_file_path_exists(dest_path) == False:
                os.mkdir(dest_path)
            generate_recursive(item_path, template, dest_path)
        else:
            raise TypeError("item is neither a file or a directory")