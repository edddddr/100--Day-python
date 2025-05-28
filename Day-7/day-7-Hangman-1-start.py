import random
import words

display = []
chosen_word = random.choice(words.word_list)
end_of_game = False
stage = ["Hangman", "Hangm", "Hang", "Ha", "H"]
lives = 4


guessed_words = []


for n in range(len(chosen_word)):
    display+="_"

print(f"The chosen word is : {chosen_word}")

while not end_of_game:
    guess = input("Guess a word : ").lower()

    if guess in guessed_words:
        print(f'"{guess}" word is alrady guessed befor, guess again!')
    if guess not in chosen_word:
        print(f' "{guess}" letter is not in the word  ')

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    
    if not guess in display:
        print(stage[lives])
        print(lives)
        guessed_words += guess
        if lives == 0:
            print("You lose!")
            end_of_game = True
        lives = lives -1


    print(display)

    if not "_" in display:
        end_of_game = True
        print("You win! ")
    




