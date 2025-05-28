import random


words = ["ardvark", "baboon", "camel" ]
chosen_word = random.choice(words)
end_of_game = False

display = []



for n in range(len(chosen_word)):
    display+="_"

print(f"The chosen word is : {chosen_word}")

while not end_of_game:
    guess = input("Guess a word : ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    print(display)

    if not "_" in display:
        end_of_game = True
        print("You win! ")





