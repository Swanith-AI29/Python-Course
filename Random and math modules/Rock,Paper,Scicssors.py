import random
while True:
    user=input("Welcome to the Rock,Paper,Scissors game!now enter a coice to beat the computer.").lower()
    actions=("Rock","Paper","Scissors")
    computer=random.choice(actions)
    print(f"\nYou had chosen {user},Computer had chosen {computer}.\n")
    print("Try putting between the options give by us.if that is also not workoing make sure your speeling is right.")
    if user==computer:
        print("You both have chosen{user} so it is a tie." )
    elif user=="rock":
        if computer=="scissors":
            print("Rock smashes scissors .You have won the game!")
        else:
            print("Paper covers rock.You have lost the game!")
    elif user=="scissors":
        if computer=="paper":
            print("Scissors cut paper.You have won the game!")
        else:
            print("Rock smahes scissors.You have lost the game!")
    elif user=="paper":
        if computer=="rock":
            print("Paper covers rock.You have won the game!")
        else:
            print("Scissors cut parer.You have lost the game")
    print("If you have won this game you are a true mastermind.Well if you have lost no worries.Try again!")