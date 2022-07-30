#importing random package to use it module
import random

def guess(x):
    '''
    (int) -> NoneType

    generates a random number between 1, x and ask user to guess the number, prints
    some hints according to the guess input, until user enters the random number.
    '''
    #generating a random number using randint func
    random_number = random.randint(1, x)

    #intialising user guess as 0
    guess = 0
    # repeating the process until user guess equals random number
    while guess != random_number:
        #taking user input
        guess = int(input(f" Guess a number between 1 and {x} : "))
        #giving user a hint based on conditions
        if guess < random_number:
            print("Sorry, guess again. Too low. ")
        elif guess > random_number:
            print("Sorry, guess again. Too high")

    print(f"Yay! congrats you have guessed the number {random_number} correctly!!!")

guess(10)