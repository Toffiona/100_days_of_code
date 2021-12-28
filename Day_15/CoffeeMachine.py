from art import logo
print(logo)
from Menu import MENU, resources
revenue = 0

# Check reseources report
def resources_report(resources, revenue):
    """ Check how much water, milk and coffee remaining in resources"""
    resources["money"] = revenue
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    # for items, amounts in resources.items():
    #     print(f"{items}: {amounts}")

def resources_used(user_coffee):
    """How much water, milk and coffee used to make the coffee"""
    water_used = user_coffee["ingredients"]["water"]
    milk_used = user_coffee["ingredients"]["milk"]
    coffee_used = user_coffee["ingredients"]["coffee"]
    return water_used, milk_used, coffee_used

# Check if it is enough resources to make coffee
def check_resources(user_coffee, resources):
    """Compare ingredients required to make the coffee with ingredients available in resources """
    for item in user_coffee["ingredients"]:
        if user_coffee["ingredients"][item] <= resources[item]:
            return True
        else:
            print(f"There is not enough {item}")
            return False

machine_is_off = False
#TODO1b: prompt to serve the next customer 
while machine_is_off == False:
    print("Machine status: ON")
    #TODO1a: ask user what coffee they want
    coffee = input("What coffee ☕ would you like? (espresso/latte/cappuccino): ").lower()
    #TODO2: For maintainer, enter off to turn off machine. 
    #The code should end execudtion
    if coffee == "off":
        machine_is_off = True
        print("Out of order. Machine under maintainance")
    #TODO3: if user enter "report", it should show the current resources value
    elif coffee == "report":
        resources_report(resources, revenue)
    #TODO4a: customer order coffee
    #confirm coffee and price of the coffee  
    else:    
        user_coffee = MENU[coffee]
        print(user_coffee)
        print(f"You have selected a cup of {coffee}")
        coffee_price = user_coffee["cost"]
        print(f"Your coffee price is {coffee_price}")

        #TODO4b: check if enough resources, ask user to insert coins
        enough_resources = check_resources(user_coffee, resources)
        #TODO5a: if enough resources, prompt user to insert coins
        #calculate money user inserts
        if enough_resources:
            print("Please insert coints")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            user_money = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
            print(f"You have inserted total: ${user_money}")

            #TODO6: Check if there is enough money
            # If enough money, cost of the coffee is added to the profit in resource
            # If not enough money, refund money and no coffee
            # if user insert more money than required, give them back the change
            if user_money >= coffee_price:
                if user_money > coffee_price:
                    change = round((user_money - coffee_price),2)
                    print(f"Here is {change} in change")
                print(f"Here is your {coffee}☕. Enjoy")
                
                #TODO7: update resources remaining and profit
                revenue = revenue + coffee_price 
                water_used, milk_used, coffee_used = resources_used(user_coffee)
                resources["water"] -= water_used
                resources["milk"] -= milk_used
                resources["coffee"] -= coffee_used
                resources["money"] = revenue
                #print(f"Ingredients remaining: {resources}")

            else:
                print("There is not enough money. Money refunded")
        else:
            print("Check resources")
            #print(resources_report(resources))

            