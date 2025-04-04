import random

def win(player, opponent):
    if (player == "rock" and opponent == "scissors") or \
           (player == "scissors" and opponent == "paper") or \
           (player == "paper" and opponent == "rock"):
        return True

def play_rps():
    choices = ["r", "p", "s"]
    player = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()
    if player not in choices:
        print("Invalid choice. Please try again.")
        return
    opponent = random.choice(choices)
    print(f"Opponent chose: {opponent}")

    if player == opponent:
        print("It's a tie!")
    elif win(player, opponent):
        print("You win!")
    else:
        print("You lose!")    

if __name__ == "__main__":
    play_rps()        