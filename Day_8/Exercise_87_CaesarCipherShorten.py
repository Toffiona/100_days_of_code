alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

#TODO-1: Combine the encrypt() and decrypt() functions 
# into a single function called caesar(). 

def ceasar(a_direction, a_text, a_shift):
    new_text = ""
    if a_direction == "decode":
            a_shift *= -1
    for letter in a_text:
        index = alphabet.index(letter)
        new_index = index + a_shift
        if new_index > 26 or new_index < -26:
            new_index = new_index % 26
        
        new_text += alphabet[new_index]
    print(f"The {a_direction}d text is: {new_text}")
        
ceasar(direction, text, shift)