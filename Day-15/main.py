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
             
