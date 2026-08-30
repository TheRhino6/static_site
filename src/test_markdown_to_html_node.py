import unittest
from blocks import *

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_unorderedblock(self):
        md = """
- this is a list
- the list continues
- endless possibilites
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>this is a list</li><li>the list continues</li><li>endless possibilites</li></ul></div>"
        )

    def test_1(self):
        node = markdown_to_html_node("**bold text**").to_html()
        #self.assertEqual(node, "<b>bold text</b>")
        print (node)

    def test_2(self):
        node = markdown_to_html_node("![alt text](/some/image.png)").to_html()
        #self.assertEqual(node, '<div><p><img src="/some/image.png" alt="alt text"></img></p></div>')
        print (node)

    def test_3(self):
        node = markdown_to_html_node("[a link](/some/path)").to_html()
        #self.assertEqual(node, '<div><p><a href="/some/path">a link</a></p></div>')
        print (node)

    def test_image(self):
        result = markdown_to_html_node("![alt text](/some/image.png)").to_html()
        print(result)