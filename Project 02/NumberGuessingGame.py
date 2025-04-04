import random
print('|-------------------------------------------|')
print('|\tGuess The Secret Number             |')
print('|Note: For exit enter number greater than 10|')
print('|-------------------------------------------|')

num = random.randint(1,10)
name = input("Enter Your Name: ")
if name=="":
    print("Please enter your Name First.")
else:
    while (True):
        # print("Cheat "+str(num))
        print("The Numbers Range is \'1 to 10\'")
        guess=int(input("Enter your Number: "))
        if guess==num:
            print("You have successfully guessed the secret number.!")
            print("Well played "+name+ "\n Game End...!")
            break
        elif guess>10:
            break
        else:
            print("Ohh ohh----Wrong Guess----Try Again...!")
            print('---------------------------------------')
            continue

