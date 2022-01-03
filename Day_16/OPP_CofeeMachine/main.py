from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
payment = MoneyMachine()
my_order = Menu()

is_on = True
while is_on == True:
    choice = input("What coffee ☕ would you like? (espresso/latte/cappuccino): ")
        
    if choice == "off":
        is_on = False
        print("Machine is under maintainance")
    elif choice == "report":
        coffee_maker.report()
        payment.report()
    else:
        my_coffee = my_order.find_drink(choice)
               
        if my_coffee:   
            if coffee_maker.is_resource_sufficient(my_coffee):
                            
                if payment.make_payment(my_coffee.cost):                   
                    coffee_maker.make_coffee(my_coffee)
                
#ANSWER

# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()
                
# is_on = True

# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like? ({options}): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
        
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#           coffee_maker.make_coffee(drink)
      