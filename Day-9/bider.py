import os

# print("Logo")
shall_continue = True

bid_dictionary=[]
highest_bider = {}


def add_bid(new_bider, new_price):
    new_bid = {}
    new_bid["name"] = new_bider
    new_bid["price"] = new_price
    bid_dictionary.append(new_bid)

def calc_bid(bids):
    highest_price = 0
    for n in bids:
        if n["price"] > highest_price:
           highest_price =  n["price"]
           highest_bider["name"]=n["name"]
           highest_bider["price"]= highest_price




while shall_continue:
    bider_name = input("What is your name?: ")
    bid_price = int(input("What is your bid?: $"))

    add_bid(new_bider =bider_name, new_price= bid_price)

    result = input("Are there any other bidders? Type 'yes' or 'no'.")
    if result == 'no':
        shall_continue = False
        calc_bid(bid_dictionary)
        print(f"The winner is {highest_bider['name']} and bid ${highest_bider['price']}.")
    else:
        os.system('cls')