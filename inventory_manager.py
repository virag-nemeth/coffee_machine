# The InventoryManager class manages the machine's resources (water, milk, coffee)
class InventoryManager:
    # Maximum capacity of each resource in the coffee machine
    MAX_CAPACITY = {
        "water": 1000,
        "milk": 800,
        "coffee": 500
    }

    def __init__(self):
        """
        Initialise the InventoryManager object with default resource levels.
        """
        self.resources = {
            "water": 700,
            "milk": 600,
            "coffee": 300
        }

    def report(self):
        """
        Print the current levels of resources (water, milk, coffee) in the machine.
        """
        print(f"Water: {self.resources['water']}ml \nMilk: {self.resources['milk']}ml \nCoffee: {self.resources['coffee']}g")

    def is_sufficient(self, order_ingredients):
        """
        Check if there are enough ingredients to make the requested drink.
        Return a list of insufficient ingredients, or an empty list if sufficient.
        """
        insufficient_items = []
        for item in order_ingredients:
            if order_ingredients[item] > self.resources[item]:
                insufficient_items.append(item) # Add any insufficient ingredients to the list
        return insufficient_items

    def deduct(self, order_ingredients):
        """
        Deduct the required ingredients from the available resources.
        """
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item] # Subtract ingredients from the resources

    def refill(self, ingredient, amount):
        """
        Refill a specific ingredient in the machine.
        Ensure that the refill does not exceed the maximum capacity.
        """
        if ingredient in self.resources:
            # Check if the refill would exceed the maximum allowed capacity
            if self.resources[ingredient] + amount > self.MAX_CAPACITY[ingredient]:
                max_addable = self.MAX_CAPACITY[ingredient] - self.resources[ingredient]
                print(f"Sorry, you can only add up to {max_addable} more {ingredient} (maximum capacity reached).")
                amount = max_addable if max_addable > 0 else 0 # Limit the refill to the maximum allowed amount
            self.resources[ingredient] += amount # Add the amount to the resource
            print(f"{ingredient.capitalize()} refilled to {self.resources[ingredient]}ml/g.")
        else:
            # If the user inputs an invalid ingredient, notify them
            print("Invalid ingredient.")
