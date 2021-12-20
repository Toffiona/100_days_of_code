# #print('Hello ' + input('What is your name'))
# print(1,330 +20)
###########################################################
# num_char = len(input('What is your name?'))
# new_num_char = str(num_char)
# print('Your name has ' + new_num_char + " charaters")
##########################################################

# print(3**2)
# #PEMDASLR: Parentheses, Exponents, Multiple, Dividion, Addition, Subtraction
# print(3*(3+3)/3-3)
# print(round(8 / 3 ,2))
# print(8 // 3)
###########################################

# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("YOu can drive")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("please pay $5")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $10")
# else:
#     print("YOu can not drive")
#####################################

# import random
# #print(random.randint(2,20))
# print(random.random() * 5)

# total = 0
# for num in range(0, 101):
#     total += num
# print(total)

# def my_function():
# print("Hello")

# my_function()

# list1 = ["a","b","c"]
# list2 = ["d","e","f"]
# print(list1 + list2)

# import Exercise_77_hangman_art
# print(Exercise_77_hangman_art.logo)

# def greet(name):
#     print("Hello" + " " +name)
#     print("How are you?" + " " + name)
#     print("Good bye" + " " + name)

# greet("Angela")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# greet_with("Fiona", "Sydney")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# greet_with(location = "Sydney", name = "Fiona")

shift = int(input("Type a shift number:\n"))
if shift > 26:
    shift = shift % 26 - 1

print(shift)