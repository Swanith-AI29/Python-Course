import random
class fruitquiz:
    def __init__(self):
        self.fruits={'apple':'red','watermelon':'green','banana':'yellow','orange':'orange'}
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruits.items()))
            print('What is the color of {}'.format(fruit))
            useranswer=input()
            if useranswer.lower()==color:
                print('correct answer')
            else:
                print('Incorrect answer')
            option=int(input('Enter 0 if you want to play again otherwise enter 1: '))
            if option: 
                break

print('Welcome to the food quiz')
fcube=fruitquiz()
fcube.quiz()