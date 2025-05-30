import os
# Calculator

def add(n1, n2):
    return n1 + n2 

def sub(n1, n2):
    return n1 - n2 

def mul(n1, n2):
    return n1 * n2 

def div(n1, n2):
    return n1 / n2 

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
    }

num1 = int(input("What's the first number? : "))
num2 = int(input("What's the second number? : "))
for symbol in operations:
    print(symbol)


operation_symbol = input("Peek operation from the line: ")

first_calculation_function = operations[operation_symbol]
answer = first_calculation_function(num1, num2)
print(f"{num2} {operation_symbol} {num2} : {answer}")

# to continue
should_continue = True
while should_continue:
    result = input(f"Type 'y' to continue calculatign with {answer} or type 'n' to exit:")
    if result == 'n':
        os.system('cls')
        exit()
    else:
        operation_symbol = input("Pick an operator : ")
        num3 = int(input("What's the next number? : "))
        second_calculation_function = operations[operation_symbol]
        answer = second_calculation_function(first_calculation_function(num1, num2,), num3)
        # print(f"{num2} {operation_symbol} {num2} : {answer}")


