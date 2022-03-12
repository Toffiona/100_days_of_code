#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp




with open("/Users/Fioka/Documents/Python/Udemy/100_days_of_code/Day_24/Mail_Merge/Input/Names/invited_names.txt", mode="r") as names:
    list_of_names = names.readlines()
    
    print(list_of_names)

    # for name in list_of_names:
    with open("/Users/Fioka/Documents/Python/Udemy/100_days_of_code/Day_24/Mail_Merge/Input/Letters/starting_letter.txt",mode="r") as template:
        template_content = template.read()
        for name in list_of_names:
            new_name = name.strip("\n")
            with open (f"/Users/Fioka/Documents/Python/Udemy/100_days_of_code/Day_24/Mail_Merge/Output/letter - {new_name}.txt", mode="w") as letter:
                content = template_content.replace("[name]", new_name)
                letter.write(content)
            print(letter)
                

    
