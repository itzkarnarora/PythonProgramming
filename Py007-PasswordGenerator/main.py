import random

# Display a welcome message
print("Welcome to the Password Generator!")

# Define character sets for password generation
smallCharacters = "abcdefghijklmnopqrstuvwxyz"
capitalCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numCharacters = "0123456789"
specialCharacters = "!@#$%^&*()_+~`|}{[]\\:;?><,./-="

# Initialize an empty list to store password characters
passwordList = []

try:
    # Get the desired number of each character type from the user
    smallChar = int(input("How many lowercase characters would you like? "))
    capitalChar = int(input("How many uppercase characters would you like? "))
    numChar = int(input("How many numbers would you like? "))
    specialChar = int(input("How many special characters would you like? "))

    # Check that all character counts are non-negative
    if any(n < 0 for n in (smallChar, capitalChar, numChar, specialChar)):
        print("Error: Character counts cannot be negative.")

    # Ensure that the requested password length is greater than zero
    elif smallChar + capitalChar + numChar + specialChar == 0:
        print("Error: Your password must contain at least one character.")

    else:
        # Randomly select the requested lowercase characters
        passwordList.extend(random.choices(smallCharacters, k=smallChar))

        # Randomly select the requested uppercase characters
        passwordList.extend(random.choices(capitalCharacters, k=capitalChar))

        # Randomly select the requested digits
        passwordList.extend(random.choices(numCharacters, k=numChar))

        # Randomly select the requested special characters
        passwordList.extend(random.choices(specialCharacters, k=specialChar))

        # Shuffle the list so the character types appear in random order
        random.shuffle(passwordList)

        # Join all selected characters to create the final password
        password = "".join(passwordList)

        # Display the generated password
        print(f"\nYour new password is:\n{password}")

# Handle invalid input when the user enters something other than a whole number
except ValueError:
    print("Error: Please enter whole numbers only.")
