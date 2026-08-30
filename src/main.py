from textnode import TextNode
from pathlib import Path
from copy_files import copy_files
from generate import *


def main():
    current_path = Path.cwd()
    copy_files(current_path)
    
    host = os.path.join(current_path, "content")
    template = os.path.join(current_path, "template.html")
    target = os.path.join(current_path, "public")
    generate_recursive(host, template, target)

if __name__ == "__main__":
    main()