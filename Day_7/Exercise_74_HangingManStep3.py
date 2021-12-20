
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

chosen_word_list = []
for n in range(len(chosen_word)):
    chosen_word_list.append("_")
print(chosen_word_list)
#TODO-1: - Use a while loop to let the user guess again.
#  The loop should only stop once the user has guessed 
# all the letters in the chosen_word and 'display' 
# has no more blanks ("_"). 
# Then you can tell the user they've won.


while "_" in chosen_word_list:
    guess = input("Guess a letter: ").lower()

    for n in range(len(chosen_word)):
        if chosen_word[n] == guess:
            chosen_word_list[n] = guess
        
    print(chosen_word_list)
print("You have won")

