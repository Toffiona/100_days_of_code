############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import art
import os
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def check_blackjack(cards_pack, your_cards):
    if cards_pack[0] in your_cards:
        if cards_pack[9] in your_cards or cards_pack[10] in your_cards or cards_pack[11] in your_cards or cards_pack[12] in your_cards:
            return True 

def draw_card(cards_pack, your_cards):
    next_card = random.choice(cards_pack)
    your_cards.append(next_card)
    scores = 0
    for card in your_cards:
        scores += card
    if cards_pack[0] in your_cards and scores > 21:
        scores -= 10
    return your_cards, scores     
                   
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
play_again = "y"
while play_again == "y":
    clearConsole()
    print(art.logo)
    your_cards = random.sample(cards,2)
    current_score = your_cards[0] + your_cards[1]
    print(f"Your cards: {your_cards}, current score: {current_score}")

    dealer_cards = random.sample(cards,2)
    print(f"Dealer first card: {dealer_cards[0]}")
    dealer_score = dealer_cards[0] + dealer_cards[1]

    if check_blackjack(cards, dealer_cards) == True:
        print("Dealer got a blackjack. Dealer wins regardless you got blackjack or not")
    elif check_blackjack(cards, dealer_cards) == False and check_blackjack(cards, your_cards) == True:
        print("You got a blackjack. You win")

    else:
        game_is_on = True
        while game_is_on == True:
            continue_draw = input("Typed 'y' to get another card, type 'n' to pass: ").lower()
             
            if continue_draw == "n":
                your_final_cards, your_final_score = your_cards, current_score
                print(f"Your final cards: {your_final_cards}, final score: {your_final_score}")
                print("Dealer turn to draw")
                        
            while continue_draw == "y":        
                your_final_cards, your_final_score = draw_card(cards, your_cards)
                print (f"your cards: {your_final_cards}, current score: {your_final_score}")
                new_continue_draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                                                
                if new_continue_draw == "n" or your_final_score > 21:
                    continue_draw = "n"
                    print(f"Your final cards: {your_final_cards}, final score: {your_final_score}")
                    print("Dealer turn to draw")
            if your_final_score > 21:
                game_is_on = False
                                    
            
                

    if dealer_score < 17:
        dealer_final_cards, dealer_final_score = draw_card(cards, dealer_cards)
        while dealer_final_score < 17:
            dealer_final_cards, dealer_final_score = draw_card(cards, dealer_cards)
        print (f"Dealer final cards: {dealer_final_cards}, final score: {dealer_final_score}")
    else:    
        dealer_final_score = dealer_score
        print (f"Dealer final cards: {dealer_cards}, final score: {dealer_final_score}")
        
    if your_final_score > 21:
        print("You went over, you loose")
    else:
        if dealer_final_score > 21:
            print("Dealer went over. You win")
        else:
            if your_final_score > dealer_final_score:
                print("You win")
            elif your_final_score < dealer_final_score:
                print("YOu loose")
            else:
                print("It's a draw")

    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


    

        


            
