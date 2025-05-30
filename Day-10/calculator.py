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
for symbol in operations:
    print(symbol)

# to continue
should_continue = True
while should_continue:
   operation_symbol = input("Peek operation from the line: ")
   num2 = int(input("What's the next number? : "))
   calculation_function = operations[operation_symbol]
   answer = calculation_function(num1, num2)
   print(f"{num2} {operation_symbol} {num2} : {answer}")

   if  input(f"Type 'y' to continue with {answer}, or 'n' to exit : ") == 'n':
        should_continue = False
        os.system('cls')       
        exit()
    


