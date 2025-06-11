from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffe_menu = Menu()
coffee_machine = MoneyMachine()


is_on = True

while is_on:
        
    option = coffe_menu.get_items()
    answer = input(f"What do you want? {option} : ")
    if option == 'off':
           is_on = False
    if option == 'report':
        coffee_maker.report() 
        coffee_machine.report() 
    else:
        type = coffe_menu.find_drink(answer)

        coffee_maker = CoffeeMaker()
        if (coffee_maker.is_resource_sufficient(type)):
                proccessed_money  = coffee_machine.process_coins()
                if coffee_machine.make_payment(proccessed_money):
                        coffee_maker.make_coffee(type)



