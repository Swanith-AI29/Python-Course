class lower():
    def __init__(self,str1):
        self.str1=str1
    def getword(self):
        print(input('Give the word to convert it into lowercase.'))
    def answerword(self):
        print('The word in lowercase is',self.str1.lower())

text=lower('SWANITH')
text.answerword()
