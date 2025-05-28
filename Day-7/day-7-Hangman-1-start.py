import random


words = ["ardvark", "baboon", "camel" ]
display = []
chosen_word = random.choice(words)
end_of_game = False
stage = ["Hangman", "Hangm", "Hang", "Ha", "H"]
lives = 4





for n in range(len(chosen_word)):
    display+="_"

print(f"The chosen word is : {chosen_word}")

while not end_of_game:
    guess = input("Guess a word : ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    
    if not guess in display:
        print(stage[lives])
        print(lives)
        if lives == 0:
            print("You lose!")
            end_of_game = True
        lives = lives -1


    print(display)

    if not "_" in display:
        end_of_game = True
        print("You win! ")
    




