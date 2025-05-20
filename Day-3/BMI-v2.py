
height = float(input("Eneter your height : "))
weight = float(input("Eneter your weight : "))

print(height, weight)

BMI =  int(weight / (height * height))

if BMI <= 18.5:
    print(f"Your BMI is {BMI}, you are Underweight")
elif BMI <= 25:
    print(f"Your BMI is {BMI}, you areNormalweight")
elif BMI <= 30:
    print(f"Your BMI is {BMI}, you areOverweight")
elif BMI <= 35:
    print(f"Your BMI is {BMI}, you areObese")
else:
    print(f"Your BMI is {BMI}, you areClinically Obese")    