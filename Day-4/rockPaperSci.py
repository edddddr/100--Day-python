import random

choosen = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor "))
ground =["Rock", "Paper", "Scissor"]

randomNum = random.randint(0, 2)

userChoosen = ground[choosen]
computerChose = ground[randomNum]

print(f'You choosed: {userChoosen}')
print(f'Computer Chose: {computerChose}')


if userChoosen == "Rock" and computerChose == "Scissor":
    print("You Win")

elif userChoosen == "Scissor" and computerChose == "Paper":
    print("You win")

elif userChoosen == "Paper" and computerChose == "Rock":
    print("You win")
elif userChoosen == computerChose:
    print("Draw")
else:
    print("You Lose")


