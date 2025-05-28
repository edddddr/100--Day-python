import random


words = ["ardvark", "baboon", "camel" ]
guess = input("enter a letter : ").lower()

chosen_word = random.choice(words)
print(f"The chosen word is : {chosen_word}")

for letter in chosen_word:
    if letter == guess:
        print("True")
    else:
        print("false")

