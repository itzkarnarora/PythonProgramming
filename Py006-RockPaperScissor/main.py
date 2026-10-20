# Rock, Paper, Scissors Game in Python

# Import the random module to let the computer make a random choice
import random

# Welcome the player to the game
print("Welcome to Rock, Paper, Scissors Game!")

# Keep the game running until the player chooses to exit
while True:

    # Randomly choose rock, paper, or scissors for the computer
    compChoice = random.choice(['rock', 'paper', 'scissors'])

    # Ask the player for their choice
    userChoice = input("Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()

    # Check if both the player and computer selected the same option
    if userChoice == compChoice:
        print(f"Both players selected {userChoice}. It's a tie!")

    # Check all possible combinations where the player wins
    elif (userChoice == 'rock' and compChoice == 'scissors') or \
         (userChoice == 'paper' and compChoice == 'rock') or \
         (userChoice == 'scissors' and compChoice == 'paper'):
        print(f"You chose {userChoice} and the computer chose {compChoice}. You win!")

    # Check all possible combinations where the computer wins
    elif (userChoice == 'rock' and compChoice == 'paper') or \
         (userChoice == 'paper' and compChoice == 'scissors') or \
         (userChoice == 'scissors' and compChoice == 'rock'):
        print(f"You chose {userChoice} and the computer chose {compChoice}. You lose!")

    # Exit the game when the player enters 'exit'
    elif userChoice == 'exit':
        print("Thanks for playing! Goodbye!")
        # Stop the while loop
        break

    # Handle any input that is not a valid choice
    elif userChoice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        # Skip to the next iteration of the loop
        continue
