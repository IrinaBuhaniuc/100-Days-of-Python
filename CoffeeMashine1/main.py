from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


#latte = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
#espresso = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
#cappuccino = MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)

is_on = True

while is_on:
    option = menu.get_items()
    choice = input(f"What would you like to trink? ({option})")

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        sufficient = coffee_maker.is_resource_sufficient(drink)
        if sufficient:
            #money_machine.process_coins()
            cost = drink.cost
            if money_machine.make_payment(cost):
                order = coffee_maker.make_coffee(drink)

        else:
            is_on = False

