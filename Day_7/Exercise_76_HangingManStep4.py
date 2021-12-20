#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track
# of the number of lives left. 
#Set 'lives' to equal 6.

lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

chosen_word_list = []
for n in range(len(chosen_word)):
    chosen_word_list.append("_")
print(chosen_word_list)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for n in range(len(chosen_word)):
        if chosen_word[n] == guess:
            chosen_word_list[n] = guess
    print(''.join(chosen_word_list))       

#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and 
    # it should print "You lose."

    #Join all the elements in the list and turn it into a String.
  
    
    if guess not in chosen_word_list:
        print("Your guess is incorrect")
        lives -= 1
        print(stages[6 - lives])
        print(f"you have {lives} lives left")
        print(''.join(chosen_word_list))

        #Check if user has got all letters.
        if lives == 0:
            end_of_game = True
            print("You lose")
        
    if "_" not in chosen_word_list:
        end_of_game = True
        print("You win")      


 