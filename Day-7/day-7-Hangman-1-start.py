import random

word_list = ["ardvark", "baboon", "camel"]

choosen_word = random.choice(word_list)

guess = input("Guess a word : ").lower()

for n in choosen_word:
    if n == guess:
        print("true")
    else: 
        print("False")


