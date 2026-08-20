import unittest
from blocktype import *

class TestBlockType(unittest.TestCase):
    def test_header(self):
        block = "##### This is the second header"
        block_type = block_to_block_type(block)
        expected_type = BlockType.HEADING
        self.assertEqual(block_type, expected_type)

    def test_code(self):
        block = "```\nthis is a code block```"
        block_type = block_to_block_type(block)
        expected_type = BlockType.CODE
        self.assertEqual(block_type, expected_type)

    def test_quote(self):
        block = "> this is possibly a quote\n> so is this but we might need to fact check\n> who knows about this one?"
        block_type = block_to_block_type(block)
        expected_type = BlockType.QUOTE
        self.assertEqual(block_type, expected_type)

    def test_unordered_list(self):
        block = "- this is a list\n- that isn't ordered\n- what is my type?\n- oops got your toungue"
        block_type = block_to_block_type(block)
        expected_type = BlockType.UNORDERED_LIST
        self.assertEqual(block_type, expected_type)

    def test_ordered_list(self):
        block = "1. hopefully this works\n2. this is an ordered list\n3. an we will keep counting\n4. i can count to four\n5. i can count no more"
        block_type = block_to_block_type(block)
        expected_type = BlockType.ORDERED_LIST
        self.assertEqual(block_type, expected_type)

    def test_paragraph_easy(self):
        block = "This is a paragraph, hopefully it will be easy because it's only one line."
        block_type = block_to_block_type(block)
        expected_type = BlockType.PARAGRAPH
        self.assertEqual(block_type, expected_type)

    def test_paragraph_medium(self):
        block = "\nthis one is a lot harder\nmixing in new lines, just \n wait until the next one"
        block_type = block_to_block_type(block)
        expected_type = BlockType.PARAGRAPH
        self.assertEqual(block_type, expected_type)

    def test_paragraph_hard(self):
        block = "1. I'm testing if the list will activate\n> hopefully it won't\n- or this one"
        block_type = block_to_block_type(block)
        expected_type = BlockType.PARAGRAPH
        self.assertEqual(block_type, expected_type)

    