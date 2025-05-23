#synaxarium of the day 
# ናትናኤል ሐዋርያዊ
# ሚናስ ባሕታዊ
# ቀርጢኖስ ስማዕት እና አራት መቶ ቅዱሳን ስማዕት

import random


# Password generator

# Random number

# Level one ++++++
print("Welcome to the PyPassword Generatoro! 🔑\n")
nr_letters = int(input("How many letter would do you like in your password? \n"))
nr_symbols = int(input("How many symbols would do you like? \n"))
nr_number =  int(input("How many numbers would do you like? \n"))

password = ''
letters = ['a','b','c','d','e','f','g', 'h', 'i', 'j']
symbols = ['!','@','#','$','%','^','&','*','(', ')']
number = [1,2,4,5,6,7,8,9,0]


for i in range(0, nr_letters):
    password += letters[random.randint(0,9)]
    
for i in range(0, nr_symbols):
    password += symbols[random.randint(0,9)]

for i in range(0, nr_number):
    password += str(number[random.randint(1,9)])


print(password)