
print("Welcome to the tip calclulator.")

totalBill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would like to give? 10, 12, or 15? "))
peaple = float(input("How many people to split the bill? "))

tip_as_percent = 1 + (tip/ 100)

print(f"Each person should pay: {round((totalBill / peaple ) * tip_as_percent, 2)}")