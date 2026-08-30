import unittest
from generate import *

class TestExtractTitle(unittest.TestCase):
    def test_extract(self):
        markdown = extract_title("# This is some markdown")
        expected = "This is some markdown"
        self.assertEqual(expected, markdown)