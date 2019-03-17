import re
class RegexLogic:

    def look_for_white_space(self, prev, post):
        if re.match('\s', prev) and re.match('\s', post):
            return True
        else:
            return False

    def extract_digits(self, line):
        return re.findall('\d+',line)
       
    def filter_punctuation(self, line):
        return line.replace(".", "")  