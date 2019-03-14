import re 
from utils.logger import Logger

class GetData:
    
    def __init__(self, name = 'numberToWords/data/textfile.txt'):
        self.name = name
    
    def open_file(self):
        try:
            f = open(self.name, "r")
            return f
        except:
            logger = Logger()
            logger.error('Cannot open file')



