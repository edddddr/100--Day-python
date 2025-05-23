#synaxarium of the day 
# ናትናኤል ሐዋርያዊ
# ሚናስ ባሕታዊ
# ቀርጢኖስ ስማዕት እና አራት መቶ ቅዱሳን ስማዕት

import random

n_l = 3
n_S = 2
n_N = 2

password = ''
nr_letters = ['a','b','c','d','e','f','g', 'h', 'i', 'j']
nr_symbols = ['!','@','#','$','%','^','&','*','(', ')']
nr_number = [1,2,4,5,6,7,8,9,0]

for i in range(0, n_l):
    password += nr_letters[random.randint(0,9)]
    
for i in range(0, n_S):
    password += nr_symbols[random.randint(0,9)]

for i in range(0, n_N):
    password += str(nr_number[random.randint(0,8)])

print(password)