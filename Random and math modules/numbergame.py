import random
playing=True 
number=str(random.randint(0,9))
print("I will generate a number from 0,9 and you have to guess one number at a time.")
print("The game ends when you get one hero.")
while playing:
    guess=input("Give me your best guess")
    if number==guess:
        print("You win the game!")
        print("The number was- ",number)
    else:
        print("Your guess wasn't right! try again")
        print("The number was-",number)