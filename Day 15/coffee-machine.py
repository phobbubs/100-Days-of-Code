MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
}

machine_on = True
resources_money = 0
resources["money"] = resources_money

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    def check_resources():
        """Check if there are enough resources"""
        if MENU[user_choice]["ingredients"]["water"] > resources["water"]:
            return "Sorry there is not enough water"
        elif MENU[user_choice]["ingredients"]["milk"] > resources["milk"]:
            return "Sorry there is not enough milk"
        elif MENU[user_choice]["ingredients"]["coffee"] > resources["coffee"]:
            return "Sorry there is not enough coffee"
        else:
            return "Please insert coins."

    def count_coins():
        """Calculate total amount of coins inserted"""
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        total_coins = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        return total_coins

    def check_transaction(total_coins, drink_cost, resources_money):
        """Check if enough money was paid for the drink"""
        if total_coins >= drink_cost:
            change = total_coins - drink_cost
            resources_money += drink_cost
            resources["Money"] = resources_money
            return round(change,2)
        else:
            return "Sorry that's not enough money. Money refunded."

    def deduct_resources(drink):
        """Deduct amount of ingredients used from resources"""
        resources["water"] = resources["water"] - MENU[drink]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[drink]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
        resources["money"] = resources["money"] + MENU[drink]["cost"]

    if user_choice == "report":
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        money = resources["money"]
        print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")

    elif user_choice == "off":
        machine_on = False

    else:
        drink = user_choice
        status = check_resources()
        if status == "Please insert coins.":
            total_coins = count_coins()
            drink_cost = MENU[drink]["cost"]
            change = check_transaction(total_coins, drink_cost, resources_money)
            if type(change) != str:
                deduct_resources(drink)
                print(f"Here is ${change} in change.")
                print(f"Here is your {drink} ☕. Enjoy!")
            elif type(change) == str:
                print(change)
        else:
            print(status)
