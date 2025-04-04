import random
from words import words

def get_valid_word(words):
    word = random.choice(words)  
    while '-' in word or ' ' in word:  # Ensure the word does not contain hyphens or spaces
        word = random.choice(words)
    return word.upper()  

# print(get_valid_word(words))  test the function

def hangman():
    word = get_valid_word(words)  # Get a random word from the list
    word_letters = set(word)  # Create a set of letters in the word
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # Set of all uppercase letters
    used_letters = set()  # Set to keep track of letters guessed by the user

    lives = 6  # Number of lives

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters:", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]  # Display the word with guessed letters
        print("Current word:", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()  # Get user input and convert to uppercase

        if user_letter in alphabet - used_letters:  # Check if the letter is valid and not guessed before
            used_letters.add(user_letter)  # Add the letter to the set of used letters
            if user_letter in word_letters:  # Check if the guessed letter is in the word
                word_letters.remove(user_letter)  # Remove the letter from the set of letters in the word
            else:
                lives -= 1  # Decrease lives if the letter is not in the word
                print("Letter is not in the word.")

        elif user_letter in used_letters:  # Check if the letter was already guessed
            print("You have already guessed that letter. Try again.")
        else:
            print("Invalid character. Please enter a valid letter.")

    if lives == 0:
        print("You died! The word was", word)
    else:
        print("Congratulations! You guessed the word", word)

hangman()  # Start the gamen
        