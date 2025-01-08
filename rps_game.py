import random

# ASCII Art for Rock, Paper, Scissors
ascii_art = {
    "rock": """
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
    """,
    "paper": """
       _______
  ---'    ____)____
             ______)
            _______)
           _______)
  ---.__________)
    """,
    "scissors": """
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
    """
}

# Game function
def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions:")
    print("- Type 'rock', 'paper', or 'scissors' to make your choice.")
    print("- Type 'exit' to quit the game.\n")

    while True:
        print("\nYour choices: rock, paper, scissors")
        user_choice = input("Enter your choice: ").lower()

        # Exit the game
        if user_choice == "exit":
            print("\nThanks for playing!")
            print(f"Final Scores: You: {user_score} | Computer: {computer_score}")
            break

        # Validate input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        # Computer's choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Display choices with ASCII art
        print("\nYou chose:")
        print(ascii_art[user_choice])
        print("Computer chose:")
        print(ascii_art[computer_choice])

        # Determine winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Display scores
        print(f"Current Scores: You: {user_score} | Computer: {computer_score}")

        # Ask to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            print(f"Final Scores: You: {user_score} | Computer: {computer_score}")
            break

# Run the game
if __name__ == "__main__":
    play_game()
