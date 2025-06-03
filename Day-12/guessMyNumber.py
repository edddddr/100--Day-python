import random

random_guess =  random.randint(1, 101)


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




from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

