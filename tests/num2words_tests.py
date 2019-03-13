import unittest
import numberToWords.number_to_words 
class TestNumberToWords(unittest.TestCase):

    def test_numberToWords(self):
        self.assertEqual(numberToWords.number_to_words.NumberToWords.to_words(576) , "five hundred and thirty six")
        self.assertEqual(numberToWords.number_to_words.NumberToWords.to_words(9121) , "nine thousand one hundred and twenty one")
        self.assertEqual(numberToWords.number_to_words.NumberToWords.to_words(10022) , "ten thousand and twenty two")