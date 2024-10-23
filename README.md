# coffee_machine
# Coffee Machine Project

Welcome to the Coffee Machine project! This started as a simple coffee-making program using a procedural coding approach, but later, I refactored the whole thing into an Object-Oriented Programming (OOP) structure to improve flexibility and modularity. Below, I’ll walk you through both versions: the original **non-OOP version** and the new **OOP refactor**. I’ll also share some reflections on why I made these changes and what I learned in the process.

## Virtual Coffee Machine (Non-OOP Version)

The first version of this project is your classic procedural code. Everything is laid out in functions, and the resources and menu items are just dictionaries. This version works perfectly fine—it can brew coffee, take payments, and manage resources—but as the code grows, it can start to get a little messy and harder to maintain.

### What it Does:

- **Menu**: The coffee machine has three options: espresso, latte, and cappuccino. The ingredients and prices for each are stored in a dictionary.
- **Resources**: Another dictionary tracks how much water, milk, and coffee are left in the machine.
- **Payments**: Users can "insert" coins (quarters, dimes, nickels, pennies) and the program calculates if they’ve inserted enough to pay for their coffee.
- **Making Coffee**: The program checks if there are enough ingredients for the selected coffee, and if there are, it deducts those ingredients and serves the coffee.
- **Refilling**: If you run out of an ingredient, you can refill it (up to a certain maximum capacity, of course).

### Structure:

All the functionality is packed into functions:

- `report()` prints the current resource levels.
- `is_resource_sufficient()` checks if there are enough ingredients for the requested coffee.
- `process_coins()` handles coin input and calculates the total.
- `is_transaction_successful()` verifies that the payment is enough to cover the cost.
- `make_coffee()` prepares the drink and deducts ingredients from the resources.
- `refill()` lets the user refill the machine with more ingredients.

### Reflection on the Non-OOP Version:

While this version works and does its job, as the project grows, it becomes harder to maintain. The more functions and variables you have, the more tangled everything gets. If you wanted to add more drinks or features, you’d have to dig through a bunch of code. That’s why I decided it was time to refactor the whole thing into OOP.

## OOP Refactor

Now, let’s talk about the OOP version. I refactored the code to practice using OOP, and I have to say, this project was the perfect candidate for restructuring. The OOP version makes it easier to extend functionality, add new features, and keep everything organised. The idea behind OOP is to break down the functionality into **objects** that interact with each other. In this case, the coffee machine became an object that can process drinks, handle payments, and manage resources. This approach makes the code more **modular** (everything is broken into neat little pieces) and **scalable** (easier to add new features).

### What Changed?

Instead of cramming everything into one file, I split the code into several classes, each with its own responsibility:

1. **`coffee_machine.py`**: This is the heart of the machine, where the `CoffeeMachine` class brings everything together. It handles user interactions and links up the different parts (like the inventory and payment systems).
2. **`drink.py`**: This file defines the `Drink` class, which represents each type of coffee, including its ingredients and price.
3. **`inventory_manager.py`**: The `InventoryManager` class tracks and manages resources (water, milk, coffee) and handles refills.
4. **`payment_processor.py`**: The `PaymentProcessor` class manages the money side of things, processing coins and checking if the payment is sufficient.

### How It Works:

Now, instead of calling a bunch of functions, the code works with objects:

```python
coffee_machine = CoffeeMachine()  # Create an instance of the CoffeeMachine
coffee_machine.run()  # Start the machine

```

Each class does its part:

- `Drink` holds the info about the coffee.
- `InventoryManager` keeps track of ingredients.
- `PaymentProcessor` handles the money.
- `CoffeeMachine` ties it all together and manages user interactions.

### Reflection on the OOP Version:

Switching to OOP was definitely a great learning experience. I wanted to see how I could restructure a project I’d already built and add some extra features (like handling refills more gracefully) using OOP principles. The result? The code is way more organised, easier to extend, and just feels cleaner.

In hindsight, OOP is overkill for a project this small, but it was totally worth it as an exercise. Now, if I ever want to add more drinks or make the payment system more complex (like adding credit card payments or customer accounts), it will be so much easier to do.

### What I Learned:

- **Modularity**: Splitting everything into separate classes helps keep the code clean and organised.
- **Maintainability**: It’s easier to fix bugs or add new features when the code is broken into smaller, self-contained pieces.
- **Scalability**: Even though this is a small project, OOP will really shine if I ever expand the coffee machine with more functionality.

---

### Conclusion:

The transition from procedural to OOP wasn’t just about making the code prettier; it was about learning how to structure projects in a more scalable and maintainable way. Both versions of the code work, but the OOP version opens the door to future enhancements and is much easier to manage. Plus, it was fun to break down the coffee machine into logical pieces and see how they could interact in a clean, organised way.

Thanks for checking out my Coffee Machine project!
