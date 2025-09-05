import random 
import time
number=random.randint(1,100)
def intro():
    print('May i ask your name.')
    global name
    name=input()
    print(name+',We are going to play a game.I am thinking of a number between 1-100')
    if number%2==0:
        x='even'
    else:
        x='odd'
    print('This is an {} number'.format(x))
    time.sleep(0.5)
def pick():
    guesstaken=0
    while guesstaken<6:
        time.sleep(0.25)
        enter=input('Guess: ')
        try:
            guess=int(enter)
            if guess<=100 and guess>=1:
                guesstaken=guesstaken+1
                if guesstaken<6:
                    if guess<number:
                        print('Guess of the number is too low.')
                    if guess>number:
                        print('The guess of the number is too high.')    
                    if guess!=number:
                        time.sleep(0.5)
                        print('Try again')
                    if guess==number:
                        break
            if guess>100 or guess<1:
                print('The number is not in the range!')
                time.sleep(0.25)
                print('Please enter a number between 1-100.')
        except:
            print("I don't think that "+enter+'is a number') 
    if guess==number:
        guesstaken=str(guesstaken)
        print('Good job! {} You gussed my number in {} guesses.format(name,guesstaken)')
    if guess!=number:
        print('Sorry the number i was thinking of was '+str(number))
playagain='yes'
while playagain=='yes' or playagain=='y' or playagain=='Y':
    intro()
    pick()
    print('Do you want to play again?')
    playagain=input()