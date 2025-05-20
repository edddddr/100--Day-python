
print("Welcome to Python Pizza Deliveries")

size = input("What size pizza do you want? S, M, L ")
add_pepperoni = input("Do you want paperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
elif size == 'L':
    bill = 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    elif size == 'M':
        bill += 3

if extra_cheese == 'Y':
    bill +=3

print(f"Your final bill is: {bill}.")