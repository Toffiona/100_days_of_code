# I was reading this article by Tim Urban - Your Life in Weeks and realised 
# just how little time we actually have.

# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many 
# days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message 
# with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_in_int = int(age)
x = (90 - age_in_int) * 365
y = int(x * 52 / 365)
z = int(x * 12 /365)
messgae = f"You have {x} days, {y} weeks, and {z} months left"
print(messgae)