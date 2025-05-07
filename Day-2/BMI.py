# we are going build BMI calculator
# to do the calculation we have two requirments width and height
# Formula is width / height * height(2)

 

height = float(input("Eneter your height : "))
weight = float(input("Eneter your weight : "))

print(height, weight)

BMI =  int(weight / (height * height))

print("Your BMI is : ", BMI)