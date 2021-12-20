name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
both_name = (name1 + name2).lower()
print(both_name)
count_t = both_name.count('t')
count_r = both_name.count('r')
count_u = both_name.count('u')
count_e = both_name.count('e')
total_true = count_t + count_r + count_u + count_e
#print(total_true)

count_l = both_name.count('l')
count_o = both_name.count('o')
count_v = both_name.count('v')
count_e = both_name.count('e')
total_love = count_l + count_o + count_v + count_e
#print(total_love)

love_score = int(str(total_true) + str(total_love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")