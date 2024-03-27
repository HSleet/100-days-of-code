import os
from time import sleep

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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    """Prints the current resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    if profit > 0:
        print(f"Money: ${profit}")
    input("Press enter to continue...")
    
    
def check_resources(drink):
    condition_not_met = []    
    resources_needed = MENU[drink]["ingredients"]
    for resource in resources_needed:
        if resources_needed[resource] > resources[resource]:
            print(f"Sorry, there is not enough {resource}.")
            condition_not_met.append(False)
    
    if False in condition_not_met:
        return False
    return True
    

def process_coins():
    quarters = int(input("How many quarters?: ")) * .25
    dimes = int(input("How many dimes?: ")) * .10
    nickles = int(input("How many nickles?: ")) * .05
    pennies = int(input("How many pennies?: ")) * .01
    total = quarters + dimes + nickles + pennies
    return total
    

def make_transaction(drink, total):
    global profit
    cost = MENU[drink]["cost"]
    change = total - cost
    profit += cost
    if total < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return -1
    else:
        return round(change, 2)


def make_coffee(drink):
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {drink} ☕. Enjoy!")
    
    
def coffee_machine():
    os.system("cls")
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == "report":
        report()
        coffee_machine()
    elif prompt == "off":
        print("Turning off...")
        sleep(.5)
    else:
        if check_resources(prompt):
            total = process_coins()
            change = make_transaction(prompt, total)
            if change > 0:
                print(f"Here is ${change} in change.")
            make_coffee(prompt)
        input("Press enter to continue...")
        coffee_machine()
         
        
        
if __name__ == "__main__":
    coffee_machine()
