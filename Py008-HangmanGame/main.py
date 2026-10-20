# Welcome to Python Hangman Game
import random

# Display the game title.
hangman_title = r"""
 _   _                                        
| | | |                                       
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __ 
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                     
                   |___/                      
"""
print(hangman_title)

# Hangman stages, displayed according to the remaining lives.
stages = [
    r'''
       +---+
           |
           |
    =========
       |   |
       O   |
      /|\  |
      / \  |
           |
           |
    =========
    ''',
    r'''
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
           |
    =========
    ''',
    r'''
       +---+
       |   |
       O   |
      /|\  |
           |
           |
           |
    =========
    ''',
    r'''
       +---+
       |   |
       O   |
      /|   |
           |
           |
           |
    =========
    ''',
    r'''
       +---+
       |   |
       O   |
       |   |
           |
           |
           |
    =========
    ''',
    r'''
       +---+
       |   |
       O   |
           |
           |
           |
           |
    =========
    ''',
    r'''
       +---+
       |   |
           |
           |
           |
           |
           |
    =========
    '''
]
print(stages[0])

# List of possible words for the game.
wordList = [
    "mouse", "apple", "chair", "phone", "table",
    "plant", "bread", "water", "house", "light",
    "earth", "stone", "cloud", "river", "ocean",
    "tiger", "horse", "sheep", "whale", "eagle",
    "human", "brain", "heart", "smile", "laugh",
    "music", "piano", "drums", "dance", "paint",
    "sword", "knife", "spear", "armor", "crown",
    "clock", "watch", "glass", "plate", "spoon",
    "shirt", "pants", "shoes", "dress", "skirt",
    "grape", "lemon", "mango", "peach", "melon",
    "berry", "onion", "spice", "honey", "cream",
    "truck", "plane", "train", "wheel", "motor",
    "robot", "light", "cable", "board", "screen",
    "magic", "ghost", "witch", "fairy", "angel",
    "world", "space", "stars", "comet", "venus",
    "money", "coins", "banky", "trade", "price",
    "grass", "trees", "woods", "field", "flame",
    "snake", "shark", "zebra", "camel", "koala",
    "towel", "brush", "soap", "shelf", "pillow"
]

# Set the initial number of lives and choose a random word.
lives = 6
chosenWord = random.choice(wordList)

# Create a placeholder containing one dash for each letter.
placeHolder = ""
wordLength = len(chosenWord)

for position in range(wordLength):
    placeHolder += "-"

gameOver = False
correctLetters = []

# Continue the game until the player wins or loses.
while not gameOver:
    print(f"***************{lives}/6 Lives Left***************")

    userGuess = input("Guess a letter: ").lower()
    print(userGuess)

    # Inform the player if the letter has already been guessed.
    if userGuess in correctLetters:
        print(f"You have already guessed {userGuess}")

    display = ""

    # Reveal correctly guessed letters and hide the remaining letters.
    for letter in chosenWord:
        if letter == userGuess:
            display += letter
            correctLetters.append(userGuess)
        elif letter in correctLetters:
            display += letter
        else:
            display += "-"
    print(display)

    # Reduce a life when the guessed letter is not in the word.
    if userGuess not in chosenWord:
        lives -= 1

        if lives == 0:
            gameOver = True
            print("You Lose!")

    # End the game when every letter has been revealed.
    if "-" not in display:
        gameOver = True
        print("You Win!")

    # Display the hangman stage matching the remaining lives.
    print(stages[lives])
