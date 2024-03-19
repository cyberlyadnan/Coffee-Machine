from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



# menu_item=MenuItem()
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_game = True


while is_game:
    item= menu.get_items()
    choice = input(f"What would You lIke? ({item}) : ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_game = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
















