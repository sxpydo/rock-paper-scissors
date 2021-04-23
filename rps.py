from random import randint


t = ["Rock", "Paper", "Scissors"]


computer = t[randint(0,2)]


player = False

while player == False:

    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("It's a tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("Phew! You win!", player, "crushes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("Ouch! You lose!", computer, "cuts", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("Crunch! You lose...", computer, "crushes", player)
        else:
            print("Snap! You win!", player, "cuts", computer)
    else:
        print("404 Check your spelling!")
    
    player = False
    computer = t[randint(0,2)]