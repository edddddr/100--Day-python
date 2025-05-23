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

passwordList = ''
password = ''
letters = ['a','b','c','d','e','f','g', 'h', 'i', 'j']
symbols = ['!','@','#','$','%','^','&','*','(', ')']
number = [1,2,4,5,6,7,8,9,0]
passwordList 


for i in range(0, nr_letters):
    passwordList += letters[random.randint(0,9)] + ' '
    
for i in range(0, nr_symbols):
    passwordList += symbols[random.randint(0,9)] + ' '

for i in range(0, nr_number):
    passwordList += str(number[random.randint(0,8)]) + ' '


passwordList = passwordList.split()
 
random.shuffle(passwordList)
    
for char in passwordList:
    password += char


print(password)