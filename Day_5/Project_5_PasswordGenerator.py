from math import radians
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator!")

letters_in_pass = int(input("How many letter would you like to have in your password?\n"))
numbers_in_pass = int(input("How many number would you like to have in your password?\n"))
symbols_in_pass = int(input("How many symbols would you like to have in your password?\n"))

random_letters = random.sample(letters, letters_in_pass)
random_numbers = random.sample(numbers, numbers_in_pass)
random_symbols = random.sample(symbols, symbols_in_pass)

random_characters_list =[]
random_characters_list.extend(random_letters)
random_characters_list.extend(random_numbers)
random_characters_list.extend(random_symbols)

random.shuffle(random_characters_list)
# print(random_characters_list)
# print(range(0, len(random_characters_list)))

password = ""
for element in range(0,len(random_characters_list)):
    password += random_characters_list[element]
print(f"Your password generated is: {password}")





    