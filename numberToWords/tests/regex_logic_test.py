import unittest
import numberToWords.utils.regex_logic as rl

class TestRegexLogic(unittest.TestCase):
    def __init__(self):
        self.process = rl()
        
    def test_whitespace(self):
        self.assertTrue(self.process.look_for_white_space(' ',' '))
        self.assertFalse(self.process.look_for_white_space('#',' '))
        self.assertFalse(self.process.look_for_white_space('','#'))
    
    def test_extract_digits(self):
        self.assertEqual(self.process.extract_digits('Blah Blah 132 Blah'), '132')
    
    def test_filter_punctuation(self):
        self.assertEqual(self.process.extract_digits('Blah. Blah. Blah.'), 'Blah Blah Blah')