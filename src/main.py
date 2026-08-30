from textnode import TextNode
from pathlib import Path
from copy_files import copy_files
from generate import *


def main():
    textnode = TextNode("Hello, World!", text_type="plain", url="https://www.boot.dev")
    print (textnode)

    current_path = Path.cwd()
    copy_files(current_path)
    
    host = os.path.join(current_path, "content/index.md")
    template = os.path.join(current_path, "template.html")
    target = os.path.join(current_path, "public/index.html")
    generate_page(host, template, target)

if __name__ == "__main__":
    main()