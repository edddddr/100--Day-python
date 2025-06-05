from art import logo, vs 
from game_data import data 
import os
import random 


RIGHT = "right"
WRONG = "wrong"

print(logo) 

def generator():
    return random.randint(0, len(data) -1)

def option(random_number1,random_number2):
    print(f"Compare A: {data[random_number1]["name"]}, a {data[random_number1]["description"]}, from {data[random_number1]["country"]}.")
    print(vs)
    print(f"Against B: {data[random_number2]["name"]}, a {data[random_number2]["description"]}, from {data[random_number2]["country"]}")

    return input("Who has most follower? Type 'A' or 'B' : ")


def compare(A,B):
    correct_Answer = ''
    if A >B:
        correct_Answer = 'A'
        print("A is the answer")
    else:
        correct_Answer = 'B'
        print("B is the answer")
    return correct_Answer
         
    


def game():
    is_correct = 'right'
    score = 0

    while is_correct != 'wrong':
        if score !=0:
            print(f"You're {RIGHT}! Current score is : {score}")

        random_number1 = generator()
        random_number2 = generator()

        answer = option(random_number1, random_number2)

        correct_answer = compare(data[random_number1]["follower_count"], data[random_number2]["follower_count"])

        if correct_answer == answer:
            score +=1
            os.system('cls')
        else:
            is_correct = 'wrong'
            os.system('cls')
            
    if is_correct == 'wrong':
        print(f"Sorry, that's {WRONG}. Final score: {score}")



game()