import re 
from utils.logger import Logger

class GetData:

    def __init__(self, name):
        self.name = name
    
    def open_file(self):
        f = open(self.name, "r")
        return f




