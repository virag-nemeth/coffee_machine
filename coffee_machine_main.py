# Import the necessary classes to run the coffee machine
from drink import Drink
from inventory_manager import InventoryManager
from payment_processor import PaymentProcessor

class CoffeeMachine:
    def __init__(self):
        """
        Initialise the CoffeeMachine object with:
        - An instance of InventoryManager to handle resources.
        - An instance of PaymentProcessor to handle payments.
        - A menu that contains available drinks with their ingredients and costs.
        """
        self.inventory = InventoryManager() # Manage machine's resources (water, milk, coffee)
        self.payment = PaymentProcessor() # Manage transactions and track profits
        # Define the menu of available drinks
        self.menu = {
            "espresso": Drink("espresso", {"water": 50, "coffee": 18}, 1.5),
            "latte": Drink("latte", {"water": 200, "milk": 150, "coffee": 24}, 2.5),
            "cappuccino": Drink("cappuccino", {"water": 250, "milk": 100, "coffee": 24}, 3.0)
        }

    def make_coffee(self, drink):
        """
        Deduct the ingredients needed for the chosen drink and notify the user.
        """
        self.inventory.deduct(drink.ingredients) # Deduct ingredients from inventory
        print(f"Here is your {drink.name} ☕️. Enjoy!") # Serve the coffee

    def run(self):
        """
        Main loop to run the coffee machine, handling user input and operations.
        """
        machine_on = True

        # Continuously prompt the user for input while the machine is on
        while machine_on:
            user_input = input("What would you like? (espresso/latte/cappuccino): \n").lower()

            # Turn off the machine if the user types "off"
            if user_input == "off":
                machine_on = False
                print("Machine is turning off...")
            
            # Print a report of resources and profits if the user types "report"
            elif user_input == "report":
                self.inventory.report()
                self.payment.report()
            
            # Check if the input is a valid drink name
            elif user_input in self.menu:
                drink = self.menu[user_input] # Get the drink object from the menu
                insufficient_items = self.inventory.is_sufficient(drink.ingredients) # Check if there are enough resources

                # Refill if necessary until there are enough ingredients
                while insufficient_items:
                    print(f"Sorry, there isn't enough {', '.join(insufficient_items)}.")
                    top_up = input("Would you like to refill? yes or no: ").lower()
                    if top_up == "yes":
                        ingredient = input("Which ingredient would you like to refill? coffee/water/milk: ").lower()
                        amount = int(input(f"How much {ingredient} would you like to add? "))
                        self.inventory.refill(ingredient, amount) # Refill the specified ingredient
                    else:
                        break # Exit if the user doesn't want to refill
                    insufficient_items = self.inventory.is_sufficient(drink.ingredients)  # Recheck if enough ingredients are available

                # If there are enough resources, proceed with payment and coffee making
                if not insufficient_items:
                    print(f"The cost of {drink.name} is ${drink.cost}.")
                    payment = self.payment.process_coins() # Handle coin input
                    if self.payment.is_successful(payment, drink.cost): # Check if the payment is sufficient
                        self.make_coffee(drink) # Make the coffee
            else:
                # If the user input is not recognised, inform them
                print("Sorry, that drink is not available.")

# The entry point of the program, only runs when the script is executed directly
if __name__ == "__main__":
    coffee_machine = CoffeeMachine() # Create an instance of the coffee machine
    coffee_machine.run() # Start the coffee machine