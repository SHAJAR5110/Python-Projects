import random
print('|-------------------------------------------|')
print('|\tGuess The Secret Number             |')
print('|-------------------------------------------|')


def game(x):
    lower = 1
    higher = x
    feedback = ''
    while feedback != 'c':
        if lower != higher:
            guess = random.randint(lower, higher)
        else:
            guess = lower    
        print(f'Is {guess} your secret number?')
        feedback = input("Enter 'h' if the guess is too high. Enter 'l' if the guess is too low. Enter 'c' if I guessed correctly.")
        if feedback == 'h':
            higher = guess - 1
        elif feedback == 'l':
            lower = guess + 1
    print(f'Yay! I guessed your number {guess} correctly!')

game(10)
