from art import logo, vs 
from game_data import data 
import os
import random 


RIGHT = "right"
WRONG = "wrong"

print(logo) 

def generator():
    return random.randint(0, len(data) -1)
