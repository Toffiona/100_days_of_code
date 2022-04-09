#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas
data = pandas.read_csv("./Day_26/NATO ALphabets_Project/nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}


print(alphabet_dict)

user_input = input("What's your name: ").upper()
result = [alphabet_dict[letter] for letter in user_input]
print(result)



