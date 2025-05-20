
print("Welcome to Love Caculator")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

count1 = 0
count2 = 0

name1 = name1.lower()
name2 = name2.lower()

count1 += name1.count('t')
count1 += name1.count('r')
count1 += name1.count('u')
count1 += name1.count('e')

count2 += name2.count('l')
count2 += name2.count('o')
count2 += name2.count('v')
count2 += name2.count('e')

score = str(count1) + str(count2)

if score < 10 or score > 90:
    print(f"Your score is {score} and go together like coke and mentose.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
#true love


