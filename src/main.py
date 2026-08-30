import sys
from textnode import TextNode
from pathlib import Path
from copy_files import copy_files
from generate import *


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    current_path = Path.cwd()
    copy_files(current_path)
    
    host = os.path.join(current_path, "content")
    template = os.path.join(current_path, "template.html")
    target = os.path.join(current_path, "docs")
    generate_recursive(host, template, target, basepath)

if __name__ == "__main__":
    main()