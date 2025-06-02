import random
import os

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_chosen = []
computer_chosen = []

def generator():
        ch_card = []
        random1 = random.randint(0,12)
        ch_card.append(cards[random1])
        random2 = random.randint(0,12)
        ch_card.append(cards[random2])
        random3 = random.randint(0,12)
        ch_card.append(cards[random3])
        
        return ch_card



def blackjack():
    should_continue = True
    
    while should_continue:
        answer1 = input("Do you want to play BlackJack 'y' or 'n' : ")
        user_chosen = generator()
        computer_chosen = generator()
        if answer1 == 'y':
            print(f"    Your cards: [{user_chosen[0]},{ user_chosen[1]}]")
            print(f"    Computer's first card: {computer_chosen[0]}")
            answer2 = input("Type 'y' to get another card, type 'n' to pass : ")
            if answer2 == 'n':
                print(f"    Your final hand : [{user_chosen[0]}, {user_chosen[1]}], final score : {sum_of(user_chosen[0],user_chosen[1])}")
                print(f"    Computer's hand final : [{computer_chosen[0]}, {computer_chosen[1]}], final score {sum_of(computer_chosen[0], computer_chosen[1])}")

                final_result_checker(sum_of(user_chosen[0],user_chosen[1]), sum_of(computer_chosen[0], computer_chosen[1]))
              
            else:
                sum_of_user = sum_of(user_chosen[0],user_chosen[1], user_chosen[2])
                sum_of_computer = sum_of(computer_chosen[0], computer_chosen[1])

                print(f"    Your cards: [{user_chosen[0]}, {user_chosen[1]}, {user_chosen[2]}], current  score: {sum_of_user}")
                print(f"    Computer's first card: [{computer_chosen[0]}], final score {sum_of_computer}")
                print(f"    Your final hand : [{user_chosen[0]}, {user_chosen[1]}, {user_chosen[2]}], final score : {sum_of_user}")
                print(f"    Computer's hand final : [{computer_chosen[0]}, {computer_chosen[1]}], final score {sum_of_computer}")
                final_result_checker(sum_of_user, sum_of_computer)
        else:
            should_continue = False
            os.system('cls')
            exit()



# Functions
def sum_of(num1=0, num2=0, num3=0):
    sum = num1 + num2 + num3
    return sum

def final_result_checker(sum_of_user, sum_of_computer):

    if sum_of_user > 21:
        print("You wentover. You lose 😭")
    elif sum_of_user > sum_of_computer:
         print("You win")
    elif sum_of_computer > sum_of_user:
         print("You lose")
    else:
        print("Draw . . .")
         
# Function call
blackjack()



