import random

random_guess =  random.randint(1, 101)
# Asking type
print("Welcome to the number guessing Game! ")
print("I'm thinking of a number between 1 and 100. ")
type = input("Choose a difficulty. Type 'easy' or 'hard': ")


# +++++++++++++ Function defination +++++++++++++
# Attempts decrements
def attempts_dec(attempts):
    return attempts - 1

def guess(attempts):
    while attempts != 0:
        print(f"You have {attempts} attempts remaing to guess the number.")
        guessed_number = int(input("Make a guess: "))
        attempts = attempts_dec(attempts)
        if random_guess > guessed_number:
            print("Too lowe")
        elif random_guess < guessed_number:
            print("Too high")
        else:
            print(f"You got it the answer is: {random_guess}")
            return
    if attempts == 0:
        print("You've run out of guesses, you lose. ")

# Checker
if type == 'hard':
    guess(5)
else:
    guess(10)
