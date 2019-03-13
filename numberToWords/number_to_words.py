from utils.get_data import GetData
from utils.format_data import FormatData
from services.words_converter import WordsConverter

class NumberToWords:
    def __init__(self, pathToFile):
        self.data = GetData(pathToFile).open_file()
        self.format = FormatData()
        self.words_converter = WordsConverter()

    def run(self):
        read_data = self.data
        return [self.words_converter.run(self.format.filter_text_to_Int(line_item)) for line_item in read_data ]


if __name__ == '__main__':
    m = NumberToWords('numberToWords/data/textfile.txt')
    [ print(x) for x in m.run()]

