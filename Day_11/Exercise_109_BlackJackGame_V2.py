#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
import art
import os
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
    return sum(cards)

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
   #Hint 7: Inside calculate_score() check for a blackjack
    #  (a hand with only 2 cards: ace + 10) and return 0 instead
    #  of the actual score. 0 will represent a blackjack in our game.

    #Hint 8: Inside calculate_score() check for an 11 (ace). 
    # If the score is already over 21, remove the 11 and replace it with a 1.
    # You might need to look up append() and remove().
def calculate_score(cards):
    score = sum(cards)
    if 11 in cards and 10 in cards and len(cards) == 2:
        score = 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return score    
    


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def play_game():
    end_of_game = False
    print(art.logo)

    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while end_of_game == False:    
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your first cards is {user_cards}. Current score: {user_score}")
        print(f"Computer first card is {computer_cards[0]}")

        #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or 
        # if the user's score is over 21, then the game ends.
        #Hint 10: If the game has not ended, ask the user if they want to draw another card.
        # If yes, then use the deal_card() function to add another card to the user_cards List.
        #  If no, then the game has ended.
        
        #Hint 11: The score will need to be rechecked with every new card drawn 
        # and the checks in Hint 9 need to be repeated until the game ends.
        if computer_score == 0 or user_score == 0 or user_score > 21:
            end_of_game = True
        else:
            deal = input("Type 'y' to draw another card, type 'n' to pass: ").lower()
            if deal == "y":
                user_cards.append(deal_card())
            elif deal == "n":
                print("It's computer turn to draw")
                end_of_game = True

    #Hint 12: Once the user is done, it's time to let the computer play. 
    # The computer should keep drawing cards as long as it has a score less than 17.

    while computer_score !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Computer final cards is: {computer_cards}. Final score: {computer_score}")
        

    #Hint 13: Create a function called compare() and pass in the user_score and computer_score. 
    # If the computer and user both have the same score, then it's a draw.
    #  If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
    def compare(user_score, computer_score):
        if computer_score == 0:
            return "Computer got a blackjack. Computer wins"
        elif user_score == 0:
            return "You got a blackjack. You win"
        elif user_score > 21:
            return "You went over. You lose"
        elif computer_score > 21:
            return "Computer went over. You win"
        elif computer_score > user_score:
            return "You lose"
        elif computer_score < user_score:
            return "You win"
        else:
            return "It's a draw"

    print(compare(user_score, computer_score))

    #Hint 14: Ask the user if they want to restart the game.
    #  If they answer yes, clear the console and start a new
    # game of blackjack and show the logo from art.py.
    

while input("Would you like to play a game of BlackJack? 'y' or 'n': ") == "y":

    clearConsole()
    play_game()