# Python Pizza Delivery Project

# Welcome the customer to the pizza delivery service
print("Welcome to Python Pizza Deliveries!")

# Ask the customer for their preferred pizza size
size = input("What size pizza do you want? S, M, or L: \n").upper()

# Ask the customer if they want pepperoni
addPepperoni = input("Do you want pepperoni? Y or N: \n").upper()

# Ask the customer if they want extra cheese
extraCheese = input("Do you want extra cheese? Y or N: \n").upper()

# Start the bill at zero
bill=0

# Add the base price according to the selected pizza size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

# Add the pepperoni cost based on the pizza size
if addPepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Add the extra cheese cost if requested
if extraCheese == "Y":
    bill += 1

# Display the final bill
print(f"Your final bill is: \n${bill}.")
