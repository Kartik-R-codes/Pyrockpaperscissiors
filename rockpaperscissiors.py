import random

def game():
    print("\n")
    userinput = input("What will you choose?('r', 'p, 's')")

    if userinput == "r":
        inputno = 0

    elif userinput == "p":
        inputno = 1

    elif userinput == "s":
        inputno = 2

    else:
        print("Input is not valid")
        game()

    opponentno = random.randint(0, 2)

    if inputno == 0 and opponentno == 0: 
        print("Tie")
    elif inputno == 0 and opponentno == 1: 
        print("Paper wraps rock, you lose")
    elif inputno == 0 and opponentno == 2: 
        print("Rock smashes scissiors, you win") 
    elif inputno == 1 and opponentno == 0:
        print("Paper wraps rock, you win")
    elif inputno == 1 and opponentno == 1:
        print("Tie")
    elif inputno == 1 and opponentno == 2:
        print("Scissiors cuts paper, you lose")
    elif inputno == 2 and opponentno == 0:
        print("Rock smashes scissiors, you lose")
    elif inputno == 2 and opponentno == 1:
        print("Scissiors cuts paper, you win")
    elif inputno == 2 and opponentno == 2:
        print("Tie")
    game()

input("Press Enter To Start")

game()

