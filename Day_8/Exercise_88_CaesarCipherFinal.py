from Alphabet import alphabet

def caesar(a_direction, a_text, a_shift):
    new_text =""
    if a_direction == "decode":
        a_shift *= -1
    for letter in a_text:
        if letter not in alphabet:
            new_text += letter
        else:
            index = alphabet.index(letter)
            new_index = index + a_shift
            if new_index > 26 or new_index < -26:
                new_index = new_index % 26
            new_text += alphabet[new_index]
    print(f"the {a_direction}d text is {new_text}")

#TODO-1: Import and print the logo from art.py when the program starts.    
from CaesarCipherLogo import logo
print(logo)



#TODO-4: Can you figure out a way to ask the user 
# if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again
# and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

cipher_program = "Y"

while cipher_program == "Y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type a message:\n").lower()
    shift = int(input("Type a shift number:\n"))
    


 

#TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

    caesar(direction, text, shift)

    cipher_program = input("WOuld you like to start again? Y/N: ").title()

print("Goodbye")
