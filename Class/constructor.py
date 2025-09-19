class inputoutputstring():
    def __init__(self):
        self.str1=""
    def getstring(self):
        self.str1=input('Enter any word of your choice.')
    def displaystring(self):
        print('result is ',self.str1.upper())
string=inputoutputstring()
string.getstring()
string.displaystring()
