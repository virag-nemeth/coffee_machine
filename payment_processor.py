# The PaymentProcessor class handles coin input and payment transactions
class PaymentProcessor:
    def __init__(self):
        """
        Initialise the PaymentProcessor object with a starting profit of 0.
        """
        self.profit = 0

    def process_coins(self):
        """
        Ask the user for coin input and calculate the total value of the coins.
        Return the total amount entered.
        """
        print("Please insert coins.")
        try:
            # Prompt the user to enter the number of each coin
            total = int(input("How many quarters?: ")) * 0.25
            total += int(input("How many dimes?: ")) * 0.1
            total += int(input("How many nickels?: ")) * 0.05
            total += int(input("How many pennies?: ")) * 0.01
        except ValueError:
            # Handle invalid input and re-prompt the user
            print("Invalid coin amount entered. Please try again.")
            return self.process_coins() # Recur until valid input is entered
        return total

    def is_successful(self, money_received, drink_cost):
        """
        Check if the money received is sufficient for the drink.
        If successful, calculate and provide change, and add the profit.
        Return True if the transaction is successful, otherwise return False.
        """
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2) # Calculate change
            print(f"Here is ${change} in change.")
            self.profit += drink_cost # Add the drink cost to the profit
            return True
        else:
            # If not enough money was inserted, refund the money
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def report(self):
        """
        Print the total amount of money the machine has earned.
        """
        print(f"Money: ${self.profit}")
