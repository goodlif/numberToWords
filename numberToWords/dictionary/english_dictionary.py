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
               return  { 0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                         7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
                         13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                         17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
        
        @property
        def medium(self): 
                return { 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
                         7: 'seventy', 8: 'eighty', 9: 'ninety'}
        
        @property
        def large(self): 
                return { 1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion'}
        
        @property
        def zero(self): 
                return 'Zero'
        
        @property
        def hundred_split(self): 
                return 'hundred and'
        
        @property
        def word_split(self): 
                return ' '   

