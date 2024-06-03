import random
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"
def play_round():
    user_choice = input("Choose rock, paper, or scissors: ").lower()    
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        return None  # Invalid round
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("won the game")
    else:
        print("lost the game")
    return winner  
def game():
    user_score = 0
    computer_score = 0
    while True:
        winner = play_round()
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        print(f"Scores - You: {user_score}, Computer: {computer_score}")
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing!")
if __name__ == "__main__":
    game()
