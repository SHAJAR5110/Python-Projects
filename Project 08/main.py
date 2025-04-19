import string
import random

length = int(input("Enter password length (between 1 and 18): "))

# Validate length
if length < 1 or length > 18:
    print("Please enter a valid length between 1 and 18!")
else:
    print('''Choose character set for password from these options ({} times): 
    1. Letters
    2. Digits
    3. Special characters
    '''.format(length))

    characterList = ""

    # Loop to get user preferences for character set
    for _ in range(length):
        choice = int(input("Pick a number (1-3): "))
        if choice == 1:
            characterList += string.ascii_letters
        elif choice == 2:
            characterList += string.digits
        elif choice == 3:
            characterList += string.punctuation
        else:
            print("Invalid choice! Skipping this turn.")

    if characterList == "":
        print("No valid choices were made. Cannot generate password.")
    else:
        password = []
        for _ in range(length):
            randomchar = random.choice(characterList)
            password.append(randomchar)

        print("The random password is:", "".join(password))
