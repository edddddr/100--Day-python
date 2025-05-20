
print("Welcome to Treasure Island. ")
print("Your mession is finding the treasure! 🤨")
direction = input('Your are a cross road. where do you want to go? Type "left" or "right" ')



if direction == "left":
    action = input('you come to lake. There is island in the middle of the lake. Type "wait" to wait for a bout. Type "swim" to swim across. ')
    if action == "wait":
        colour_Choosen = input('You are arrive at the island unharmed. There is a hours wiht 3 doors. One red, One yellow, one blue. Which colour do you choose? ')
        if colour_Choosen == "yellow":
            print("you Win")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game Over")