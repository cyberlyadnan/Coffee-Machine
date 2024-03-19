# Coffee Machine

## Introduction

This Coffee Machine project simulates the functionalities of a coffee machine. It includes classes such as MenuItem, Menu, CoffeeMaker, and MoneyMachine to manage menu items, resources, and payments.

## Classes Overview

### MenuItem Class

**Attributes:**
- `name` (str): The name of the drink, e.g., "latte"
- `cost` (float): The price of the drink, e.g., 1.5
- `ingredients` (dictionary): The ingredients and amounts required to make the drink, e.g., {"water": 100, "coffee": 16}

### Menu Class

**Methods:**
- `get_items()`: Returns all the names of the available menu items as a concatenated string, e.g., "latte/espresso/cappuccino"
- `find_drink(order_name)`: Searches the menu for a particular drink by name. Returns a MenuItem object if it exists, otherwise returns None.

### CoffeeMaker Class

**Methods:**
- `report()`: Prints a report of all resources, e.g.,
  ```
  Water: 300ml
  Milk: 200ml
  Coffee: 100g
  ```
- `is_resource_sufficient(drink)`: Checks if the required ingredients for a drink are available. Returns True when the drink order can be made, False if ingredients are insufficient.
- `make_coffee(order)`: Deducts the required ingredients from the resources.

### MoneyMachine Class

**Methods:**
- `report()`: Prints the current profit, e.g., "Money: $0"
- `make_payment(cost)`: Accepts payment for a drink. Parameter `cost` is the cost of the drink. Returns True when payment is accepted, or False if the payment is insufficient.

## Usage

1. **Creating Menu Items:**
   ```python
   latte = MenuItem("latte", 2.5, {"water": 200, "milk": 150, "coffee": 25})
   espresso = MenuItem("espresso", 1.5, {"water": 50, "coffee": 18})
   cappuccino = MenuItem("cappuccino", 3.0, {"water": 250, "milk": 100, "coffee": 20})
   ```

2. **Managing Menu:**
   ```python
   menu = Menu()
   print(menu.get_items())  # Output: "latte/espresso/cappuccino"
   order = menu.find_drink("latte")
   ```

3. **Managing Coffee Maker:**
   ```python
   coffee_maker = CoffeeMaker()
   coffee_maker.report()  # Output: Report of available resources
   can_make_coffee = coffee_maker.is_resource_sufficient(order)
   if can_make_coffee:
       coffee_maker.make_coffee(order)
   ```

4. **Managing Money Machine:**
   ```python
   money_machine = MoneyMachine()
   money_machine.report()  # Output: "Money: $0"
   payment_accepted = money_machine.make_payment(order.cost)
   ```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/username/Coffee-Machine.git
   ```

2. Navigate to the project directory:
   ```
   cd Coffee-Machine
   ```

3. Run the main Python script:
   ```
   python main.py
   ```

## Contact

For any inquiries or issues, please contact:
- Email: cyberlyadnan@gmail.com
- GitHub: (https://github.com/cyberlyadnan)
