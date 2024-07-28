import random

while True:
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("Rock, Paper, Or Scissors?: ").lower()
        print("Computer: ", computer)
        print("Player: ",player)
        if (player == computer):
            print("Tie")
        elif player == "rock":
            if computer == "scissors":
                print("You Win")
            elif computer == "paper":
                print("You Lose")
        elif player == "paper":
            if computer == "scissors":
                print("You Lose")
            elif computer == "rock":
                print("You Win")
        elif player == "scissors":
            if computer == "rock":
                print("You Lose")
            elif computer == "paper":
                print("You Win")
        else:
            print("Invalid")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break
print("Bye!")
