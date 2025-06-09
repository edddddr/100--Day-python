# path menu

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}



def resource(flavor):
    return resources[flavor]



def ingredient_resources(flavor, type):
    return MENU[flavor]['ingredients'][type]


# coffee calculator
def calculator(quarter, dime, nickle, pennie):
    return round((quarter * 0.25) + (dime * 0.10) + (nickle * 0.05) + (pennie * 0.01), 2)



# machine
def coffee_machine(flavor):
        
        water_resources =  resource("water")
        milk_resources =  resource("milk")
        coffe_resources =  resource("coffee")

        ingredient_water_resources = ingredient_resources(flavor, "water")
        ingredient_coffe_resources = ingredient_resources(flavor, "coffee")
        if flavor != 'espresso':
            ingredient_milk_resources = ingredient_resources(flavor, "milk")

        resources["water"] = water_resources - ingredient_water_resources
        resources["coffee"] = coffe_resources - ingredient_coffe_resources
        if flavor != 'espresso':
            resources["milk"] = milk_resources - ingredient_milk_resources



        return f"Here is your {flavor} ☕. Enjoy!"
             
# def resource_checker(flavor):
#     water_resources =  resource("water")
#     milk_resources =  resource("milk")
#     coffe_resources =  resource("coffee")

#     ingredient_water_resources = ingredient_resources(flavor, "water")
#     ingredient_coffe_resources = ingredient_resources(flavor, "coffee")
#     if flavor != 'espresso':
#         ingredient_milk_resources = ingredient_resources(flavor, "milk")
    

#     if water_resources < ingredient_water_resources:
#             print('There is no enough water.')
#     elif coffe_resources < ingredient_coffe_resources:
#             print('There is no enough coffee.')
#     if flavor != 'espresso' and milk_resources < ingredient_milk_resources:
#             print('There is no enough milk.')
   


def processor(flavor):

    
    water_resources =  resource("water")
    milk_resources =  resource("milk")
    coffe_resources =  resource("coffee")

    ingredient_water_resources = ingredient_resources(flavor, "water")
    ingredient_coffe_resources = ingredient_resources(flavor, "coffee")
    if flavor != 'espresso':
        ingredient_milk_resources = ingredient_resources(flavor, "milk")
    

    if water_resources < ingredient_water_resources:
            print('There is no enough water.')
            return
    elif coffe_resources < ingredient_coffe_resources:
            print('There is no enough coffee.')
            return
    if flavor != 'espresso' and milk_resources < ingredient_milk_resources:
            print('There is no enough milk.')
            return

    quarter = int(input("How many quarters? "))
    dime = int(input("How many dimes? "))
    nickle = int(input("How many nickles? "))
    pennie = int(input("How many pennies? "))

    coins_amount =   calculator(quarter, dime, nickle, pennie)
    if coins_amount < MENU[flavor]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    elif coins_amount == MENU[flavor]['cost']:
        resources["money"] = coins_amount
        print(coffee_machine(flavor))
    elif coins_amount > MENU[flavor]['cost']:
        print(f"Here is {coins_amount - MENU[flavor]['cost']} dollars in change")
        print(coffee_machine(flavor))

switch =  True

while switch:
    result = input("What would you like? (espresso/latte/cappuccino) : ")

    
    if result == 'report':
        print("Water : ", resources['water'])
        print("Milk : ", resources['milk'])
        print("Coffee : ", resources['coffee'])
    elif result == 'espresso':
         processor(result)
    elif result == 'latte':
         processor(result)
    elif result == 'cappuccino':
         processor(result)
    elif result == 'off':
        switch = False
    else:
        print("You are entered invalid!")
