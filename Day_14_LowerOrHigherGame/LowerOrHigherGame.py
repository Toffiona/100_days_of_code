import random
from art import logo, vs
from game_data import data

print(logo)

def character(character_selected):
    name = character_selected["name"]
    description = character_selected["description"]
    follower_count = character_selected["follower_count"]
    country = character_selected["country"]
    return name, description, follower_count, country
    
 
def compare(a_character, b_character):
    
    a = a_character["follower_count"]
    b = b_character["follower_count"]
    if a > b:
        return "a" 
    else:
        return "b"
    
#random select character Aand result their name, description, follower number and country
a_character = random.choice(data)
name, description, follower_count, country = character(a_character)
print(f"Compare A: {name}, {description}, from {country}")
print(follower_count)


print(vs)


end_of_game = False
score = 0
while end_of_game == False:
#random select character B and result their name, description, follower number and country
    data.remove(a_character)   
    b_character = random.choice(data)
    name, description, follower_count, country = character(b_character)
    print(f"Against B: {name}, {description}, from {country}")
    print(follower_count)

    #User guess who has more followers
    guess = input("Who has higher followers? A or B: ").lower()
    # compare user guess and result
    result = compare(a_character, b_character)
    #If correct, count number of correct guess and continue the game
    #Character B become character A
    #random select new character B from the data list called Compare A
    #If not correct, count final number of correct guess and end the game

    from Clear_Console import clearConsole
    clearConsole()
    print(logo)

    if guess == result:
        score += 1
        print(f"It's correct. Your current score is {score}")
        data.append(a_character)
        a_character = b_character
        print(f"\nCompare A: {name}, {description}, {country}")
        print(a_character["follower_count"])
        print(vs)
    elif guess != result:
        score = score
        print(f"Sorry, it's wrong. Your final score is {score}")
        end_of_game = True  

    
