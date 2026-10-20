# Welcome to Tip Calculator!

# Ask the user for the total bill amount
totalBill = float(input("What was the total bill? $\n"))

# Ask the user for the percentage tip they want to give
tipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15? \n"))

# Ask the user how many people will split the bill
numberOfPeople = int(input("How many people to split the bill? \n"))

# Calculate the total bill including the tip and divide it among everyone
finalAmount = (totalBill + (totalBill * tipPercentage / 100)) / numberOfPeople

# Display the amount each person should pay
print(f"Each person should pay: ${finalAmount}")
