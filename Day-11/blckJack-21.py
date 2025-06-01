import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

randomNum1 = random.randint(0,12)
randomNum2 = random.randint(0,12)
randomNum3 = random.randint(0,12)
randomNum4 = random.randint(0,12)
player_chosen_1 = cards[randomNum1]
player_chosen_2 = cards[randomNum2]
computer_chosen_1 = cards[randomNum3]
computer_chosen_2 = cards[randomNum4]

user_chosen_result = [player_chosen_1, player_chosen_2]
computer_chosen_result = [computer_chosen_1, computer_chosen_2]

want_to_play = True
while want_to_play:
    response = input("Do you want to play a game Blackjack? 'y' or 'n' : ")
    if response == 'n':
        print(f"You final had : {user_chosen_result}")
        print(f"Computer final had : {computer_chosen_result}")
        
        exit()
    else:
        print(f"Your card is : {user_chosen_result}")
        print(f"Computer first card: {computer_chosen_result[0]}")
    


