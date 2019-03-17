import unittest
from numberToWords.number_to_words import NumberToWords as n2w

class TestNumberToWords(unittest.TestCase):
    def __init__(self):
        self.process = n2w()
        
    def test_numberToWords(self):
        self.assertEqual(self.process.to_words(576) , "five hundred and thirty six")
        self.assertEqual(self.process.to_words(9121) , "nine thousand one hundred and twenty one")
        self.assertEqual(self.process.to_words(10022) , "ten thousand and twenty two")