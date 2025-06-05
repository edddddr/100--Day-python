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
         
    


