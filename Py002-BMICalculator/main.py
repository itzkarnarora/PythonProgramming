# Welcome to BMI Calculator

# Ask the user to enter their weight in kilograms
personWeight = float(input("Enter your weight in kg: "))

# Ask the user to enter their height in meters
personHeight = float(input("Enter your height in meters: "))

# Calculate BMI using weight divided by height squared
bmi = personWeight / (personHeight ** 2)

# Display the BMI rounded to two decimal places
print(f"Your BMI is: {bmi:.2f}")

# Check the BMI category based on the calculated value
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
