import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def sum_of(num1=0, num2=0, num3=0):
    sum = num1 + num2 + num3
    return sum

for n in range(1,3):
    random1 = random.randint(0,12)
    user_chosen += cards[random1]
    random2 = random.randint(0,12)
    computer_chosen += cards[random2]

# def random_generator():
#     return cards(random.randint(0,12))

want_to_play = True
response2 = 'y'
while want_to_play:
    response1 = input("Do you want to play a game Blackjack? 'y' or 'n' : ")
    while response2 == 'y':
        if response1 == 'n':
            print(f"You final had : {user_chosen[0,1]} your current score : {sum_of(0,1,2)}")
            print(f"Computer final had : {computer_chosen}")
            
            exit()
        else:

            print(f"Your card is : {user_chosen} your current score : {sum_of(user_chosen[0],user_chosen[1],user_chosen[2])}")
            print(f"Computer first card: {computer_chosen[0]}")
            response2 = input("Type 'y' to get another card, type 'n' to pass : ")
            if response2 == 'n':
                print(f'your final had: {user_chosen}, final score is : {sum_of(user_chosen[0],user_chosen[1],user_chosen[2])}')





