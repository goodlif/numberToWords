from utils.logger import Logger
from dictionary.english_dictionary import EnglishDictionary as ed

class WordsConverter:
    def __init__(self):
        self.dictionary = ed()
        self.low = self.dictionary.low
        self.medium = self.dictionary.medium
        self.large = self.dictionary.large
        self.zero = self.dictionary.zero
        self.hundred_split = self.dictionary.hundred_split
        self.word_split = self.dictionary.word_split

    def run(self, num):
        try:
            if self.type_check(num):
                return self.to_words(num)
            else:
                return num
        except TypeError:
            log = Logger()
            log.error('Type error. Please check that input is of type string')
        except NameError:
            log = Logger()
            log.error('Number is not defined as input to RUN method')

    def type_check(self, num):
        try:
            if num.isdigit():
                return True
            else:
                return False
        except:
           log = Logger()
           log.error('Cannot conclude type')

    def to_words(self, num):
        try:
                number = int(num)
             
                if number == 0:
                    return self.zero
                
                if number < 20:
                    return self.low[number]
                
                if number < 100:
                    factor, remainder = divmod(number, 10)
                    return self.join_str(self.medium[factor], self.word_split, self.low[remainder])
                
                if number < 1000:
                    return self.get_divmod(number, 100, self.hundred_split)
                
                for key, name in self.large.items():
                    if number < 1000**(key + 1):
                        return self.get_divmod(number, 1000**key, name)
                    
                return 'Number exists outside of upper limit'      
        except:
           log = Logger()
           log.error('Process Error')

    def get_divmod(self, dividend, divisor, magnitude):
        try:
            factor, remainder = divmod(dividend, divisor)           
            return self.join_str(
                self.to_words(factor),
                ' ',
                magnitude,
                ' ',
                self.to_words(remainder),
            )
        except:
           log = Logger()
           log.error('An exception occured trying to sort the string')

    def join_str(self, *args):
        return ''.join(filter(bool, args))

if __name__ == '__main__':
    n = WordsConverter()
    print(n.run('66723107008'))
