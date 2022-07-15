import random

choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors?").capitalize()
    # Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("Hahaha! You lose!", computer, "covers", player)
            cpu_score += 1
        else:
            print("You are awesome Good Job!", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("Well, Try Again!", computer, "cut", player)
            cpu_score += 1
        else:
            print("Yay! You win!", player, "covers", computer)
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("I'm sorry, you suck...", computer, "smashes", player)
            cpu_score += 1
        else:
            print("You are awesome love!", player, "cut", computer)
            player_score += 1
    elif player == 'End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break
