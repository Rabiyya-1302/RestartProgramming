from CoffeeMaker import CoffeeMaker
from Menu import Menu
from MoneyMachine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on=True
while is_on:
    choice=input(
        f"What would you like?({menu.get_items()})"
    )
    if choice=="off":
        is_on=False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:

        drink = menu.find_drink(choice)

        if drink:

            if coffee_maker.is_resource_sufficient(drink):

                if money_machine.make_payment(drink.cost):

                    coffee_maker.make_coffee(drink)

        else:
            print("Drink not found.")