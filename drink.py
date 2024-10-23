# The Drink class represents a beverage with ingredients and cost
class Drink:
    def __init__(self, name, ingredients, cost):
        """
        Initialise a Drink object with:
        - name: The name of the drink (e.g., "espresso")
        - ingredients: A dictionary of required ingredients and their amounts
        - cost: The price of the drink in dollars
        """
        self.name = name # Name of the drink
        self.ingredients = ingredients # Ingredients required for the drink
        self.cost = cost # Price of the drink