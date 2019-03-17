import unittest
from numberToWords.utils import format_data as fd

class TestFormatData(unittest.TestCase):

    def test_numberToWords(self):
        self.assertEqual(fd.FormatData("The pump is 536 deep underground.") , "536")
        self.assertEqual(fd.FormatData("We processed 9121 records.") , "9121")
        self.assertEqual(fd.FormatData("Variables reported as having a missing type #65678.") , "Number Invalid")
        self.assertEqual(fd.FormatData("Interactive and printable 10022 ZIP code.") , "10022")
        self.assertEqual(fd.FormatData("The database has 66723107008 records.") , "66723107008")
        self.assertEqual(fd.FormatData("I received 23 456,9 KGs.") , "Number Invalid")