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
}

profit = 0

def report(resources):
    print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${profit}")

# TODO - 2 Return True when order can be made, False if ingredients are insufficient
def is_resource_sufficient(order_ingredients):
    """Return a list of insufficient ingredients."""
    insufficient_items = []
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            insufficient_items.append(item)
    return insufficient_items  # Return list of missing items

def alternative_is_resource_sufficient(order_ingredients):
    """Return True when order can be made, False if ingredients are insufficient"""
    """Alternative code"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there isn't enough {item}")
            return False
    return True

# TODO 3 - Process the inserted coins and return the total
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    try:
        total = int(input("How many quarters?: ")) * 0.25
        print(f"Inserted coin amount: {total}.")
        total += int(input("How many dimes?: ")) * 0.1
        print(f"Inserted coin amount: {total}.")
        total += int(input("How many cents?: ")) * 0.05
        print(f"Inserted coin amount: {total}.")
        total += int(input("How many pennies?: ")) * 0.01
        print(f"Inserted coin amount: {total}.")
    except ValueError:
        print("Invalid coin amount entered. Please try again.")
        return process_coins()  # Re-prompt user
    return total


# TODO 4 - return true when transaction is accepted and false if the money is insufficient
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round((money_received - drink_cost),2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO 5- make coffee and deduct the ingredients used
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

def refill(resources):
    """Refills the resources with the chosen amounts"""
    ingredient = input("Which ingredient would you like to refill? coffee/water/milk: ").lower()

    if ingredient in resources:
        amount = int(input(f"How much {ingredient} would you like to add? "))
        resources[ingredient] += amount
        print("Updated resource levels:")
        report(resources)
    else:
        print("Sorry, there is no such ingredient.")

# TODO 1- ask the user for input - create the logic for turning off and for printing a report
def coffee_machine(MENU, resources):
    machine_on = True

    while machine_on:
        user_input = input("What would you like? (espresso/latte/cappuccino): \n").lower()

        if user_input.lower() == "off":  # Check if the input is 'off'
            machine_on = False
            print("Machine is turning off...")
        elif user_input.lower() == "report":  # Print the report
            report(resources)
        elif user_input.lower() in MENU:  # Continue with other logic for coffee making
            drink = MENU[user_input]  # Access drink info
            # Check if there are enough resources
            insufficient_items = is_resource_sufficient(drink["ingredients"])

            # While loop for refilling until all ingredients are sufficient
            while insufficient_items:
                print(f"Sorry, there isn't enough {', '.join(insufficient_items)}.")
                top_up = input("Would you like to refill? yes or no: ").lower()
                if top_up == "yes":
                    refill(resources)
                else:
                    break  # Exit if user doesn't want to refill
                insufficient_items = is_resource_sufficient(drink["ingredients"])

            if not insufficient_items:  # Proceed if all ingredients are sufficient
                # Let the user know the total cost
                cost = drink["cost"]
                print(f"The cost of {user_input} is ${cost}.")
                # Process the coins
                payment = process_coins()
                # Check if the transaction was successful
                if is_transaction_successful(payment, drink["cost"]):
                    # Make coffee
                    make_coffee(user_input, drink["ingredients"])
        else:
            print("Sorry, that drink is not available.")

coffee_machine(MENU,resources)

