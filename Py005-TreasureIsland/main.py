# Python Treasure Island Game

# Display the Treasure Island ASCII art
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

# Welcome the player to the game
print("Welcome to Treasure Island!")

# Explain the objective of the game
print("Your mission is to find the treasure!")

# Ask the player which direction they want to take
way = input("You are at a cross road. Where do you want to go? Type 'left' or 'right': \n")

# Check if the player chooses the left path
if way == "left":
    # Ask the player whether they want to wait for a boat or swim across the lake
    swim = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: \n")
    # Check if the player chooses to wait for a boat
    if swim == "wait":
        # Ask the player which door they want to enter
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")
        # Check which door the player chooses
        if door == "yellow":
            # The yellow door leads to the treasure
            print("You found the treasure! You Win!")
        elif door == "red":
            # The red door leads to a room full of fire
            print("It's a room full of fire. Game Over.")
        elif door == "blue":
            # The blue door leads to a room of beasts
            print("You enter a room of beasts. Game Over.")
        else:
            # Handle an invalid door choice
            print("You chose a door that doesn't exist. Game Over.")
    else:
        # Swimming across the lake results in a game over
        print("You get attacked by an angry trout. Game Over.")
