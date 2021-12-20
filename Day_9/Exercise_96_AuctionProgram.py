from Day_11.art import logo
print(logo)

import os
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

#HINT: You can call clear() to clear the output in the console
more_users = "yes"
auction_dict = {}

def find_highest_bid(record):
    
    highest_bid = 0
    for name in record:
        if record[name] > highest_bid:
            highest_bid = record[name]
            winner = name

    print(f"The higest bid is {highest_bid} and the winner is {winner}")
        


while more_users == "yes":
    
    name = input("What is your name?\n").title()
    bid_price = int(input("What is your bid price? $\n"))
    auction_dict[name] = bid_price
    #print(auction_dict)
    more_users = input("Is there other users who want to bid? Yes/No?").lower()
    

    if more_users == "yes":
        clearConsole()
        
    elif more_users == "no":
        find_highest_bid(auction_dict)
