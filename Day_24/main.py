# # need to close the file after open

# file = open("./Day_24/file.txt")
# contents = file.read()
# print(contents)

# file.close()


# ##############OR###############
# #no need to close the file 

# with open("./Day_24/file.txt") as file:
#     contents = file.read()
#     print(contents)


# #Write on file and replace exiiting file
# with open("./Day_24/file.txt", mode="w") as file:
#     file.write("new text")

#Write and add text to existing file
#use absolute directory
# with open("/Users/Fioka/Desktop/file.txt", mode="a") as file:
#     file.write("\nNice to meet you3")

#use relative directory
with open("../../../../Desktop/file.txt", mode="a") as file:
    file.write("\nNice to meet you4")

# C:\Users\Fioka\Desktop
# C:\Users\Fioka\Documents\Python\Udemy\100_days_of_code\Day_24

