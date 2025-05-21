import random

name_string = input("Give me everybody's names, separeted by a comma. ")

names = name_string.split(',')

len_list = len(names)

person = random.randint(0,len_list)

print(f"{names[person]} is going ot by the meal today! ")