import re
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown:
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a [link](https://www.boot.dev)")
        self.assertListEqual([("link", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_2(self):
        matches = extract_markdown_links("This is text with a [link](https://www.boot.dev) and another [link](https://www.example.com)")
        self.assertListEqual([("link", "https://www.boot.dev"), ("link", "https://www.example.com")], matches)

    def test_extract_markdown_images_2(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image", "https://i.imgur.com/zjjcJKZ.png")], matches)