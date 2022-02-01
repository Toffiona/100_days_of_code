import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100")
number = random.randint(1, 100)
print(number)

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


if difficulty_level == "easy":
    attempt_no = 10  
    print(f"You have {attempt_no} attempts")      
elif difficulty_level == "hard":
    attempt_no = 5
    print(f"You have {attempt_no} attempts")
    



def compare(guess_number, computer_number, attempt):
    """ compare user number and result and return either the guessed number is lower or higher than result """
    if guess_number < computer_number and attempt > 1:
        attempt -= 1
        return f"Too low.\nGuess again.\nYou have {attempt} attempt(s) remaining"
    elif guess_number > computer_number and attempt > 1:
        attempt -= 1
        return f"Too high.\nGuess again.\nYou have {attempt} attempt(s) remaining"
    else:
        return f"You run out of guesses. You loose"
    
        


end_of_game = False
attempt_used = 0
while end_of_game == False and attempt_used <= attempt_no:
    guess = int(input("Make a guess: "))
    
    if guess == number:
        end_of_game = True
        print(f"You got it. The number is {number}") 
    else:
        result = compare(guess, number, attempt_no)
        print(result)
        attempt_no -= 1
                
        if attempt_no == 0 and guess != number:
            end_of_game = True
            #print("You run out of guesses. You loose")
        
        

#############################################################
#############################################################

# #Answer
# from random import randint
# from art import logo

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()

