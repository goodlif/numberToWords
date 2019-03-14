import re
from utils.logger import Logger

class FormatData:

    def filter_text_to_Int(self, text):
        filtered = self.filterPunctuation(text)
        digit = self.extract_digits(filtered)
        
        return self.format(digit, filtered, digit)

        
    def format(self, digit, item, text):
        try:
            size = len(digit)

            if size == 0:
                    return 'No Number'
            elif size > 1:
                    return 'Number Invalid'
            else:
                    pos = item.index(text[0])
                    b = pos - 1
                    a = pos + len(text[0])
                    before = item[b]
                    after = item[a]

                    if self.look_for_white_space(before, after):
                        return text[0]
                    else:
                        return 'Number Invalid'
        except:
            log = Logger()
            log.error('Something has gone wrong with the formatting')

    def look_for_white_space(self, prev, post):
        if re.match('\s', prev) and re.match('\s', post):
            return True
        else:
            return False

    def extract_digits(self, line):
        return re.findall('\d+',line)
       
    
    def filterPunctuation(self, line):
      return line.replace(".", "")  
