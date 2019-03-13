
from dictionary.english_dictionary import EnglishDictionary as ed

class WordsConverter:
    def __init__(self):
        self.low = ed().low
        self.medium = ed().medium
        self.large = ed().large
        self.zero = ed().zero
        self.hundred_split = ed().hundred_split
        self.word_split = ed().word_split

    def run(self, num):
        try:
            if self.type_check(num):
                return self.to_words(num)
            else:
                return num
        except TypeError:
            print('Type error. Please check that input is of type string')
        except NameError:
            print('Number is not defined')

    def type_check(self, num):
        try:
            if num.isdigit():
                return True
            else:
                return False
        except:
            print('Cannot conclude type')

    def to_words(self, num):
        try:
                print(ed.large)
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
            print('Process Error')

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
            print('An exception occured trying to sort the string')

    def join_str(self, *args):
        return ''.join(filter(bool, args))

if __name__ == '__main__':
    n = WordsConverter()
    print(n.run('66723107008'))
