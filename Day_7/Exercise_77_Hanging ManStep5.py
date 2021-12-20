import random
from Hangman_word import word_list
chosen_word = random.choice(word_list)
print(f"The chosen word is: {chosen_word}")

from Hangman_art import logo, stages
print(logo)

chosen_word_list = []
for n in range(len(chosen_word)):
    chosen_word_list.append("_")
print(chosen_word_list)

lives = 6
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for n in range(len(chosen_word)):
        if chosen_word_list[n] == guess:
            print("You have already chosen this letter")

    for n in range(len(chosen_word)):
        if chosen_word[n] == guess:
            chosen_word_list[n] = guess
    print("".join(chosen_word_list))

    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lost a life")
        lives -= 1
        print(stages[6 - lives])
        print("".join(chosen_word_list))

    if lives == 0:
        end_of_game = True
        print("You lose")
    
    if "_" not in chosen_word_list:
        end_of_game = True
        print("You win")



            