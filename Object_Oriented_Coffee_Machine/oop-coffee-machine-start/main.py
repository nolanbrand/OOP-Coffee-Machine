from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while coffee_machine_on:

    user_choice = input(f"What would you like? {menu.get_items()}: ").lower()

    if user_choice == 'off':
        coffee_machine_on = False
    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(user_choice) is not None:
        user_drink = menu.find_drink(user_choice)
        is_sufficient = coffee_maker.is_resource_sufficient(user_drink)
        if is_sufficient:
            enough_money = money_machine.make_payment(user_drink.cost)
            if enough_money:
                coffee_maker.make_coffee(user_drink)
    else:
        continue



