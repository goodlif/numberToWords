from dictionary.dictionary import Dictionary


class EnglishDictionary(Dictionary):        
        
        def __init__(self):
                self._low  = None
                self._medium = None
                self._large = None
                self._zero = None
                self._hundred_split = None
                self._word_split = None

        @property
        def low(self): 
                return self._low
        
        @low.setter
        def low(self): 
                self._low =  { 0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                     7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
                    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
        
        @property
        def medium(self): 
                return self._medium
        
        @medium.setter
        def medium(self): 
                self._medium =  { 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
                    7: 'seventy', 8: 'eighty', 9: 'ninety'}
        
        @property
        def large(self): 
                return self._large
        
        @large.setter
        def large(self): 
                self._large = { 1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion'}
        
        @property
        def zero(self): 
                return self._zero
        
        @zero.setter
        def zero(self): 
                self._zero = 'Zero'
        
        @property
        def hundred_split(self): 
                return self._hundred_split
        
        @hundred_split.setter
        def hundred_split(self): 
                self._hundred_split = 'hundred and'
        
        @property
        def word_split(self): 
                return self._low
        
        @word_split.setter
        def word_split(self): 
                self._word_split = ' '   