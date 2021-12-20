alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

#TODO-1: Create a function called 'encrypt'
# that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter 
# of the 'text' forwards in the alphabet by the shift amount 
# and print the encrypted text. 
def encrypt(a_text, a_shift):
    if shift > 26:
        print("It is invalid shift number")
    else:
        encrypted_text = ""
        for letter in a_text:
            index = alphabet.index(letter)
            new_index = index + a_shift
            if new_index > 26 or new_index < -26:
                new_index = new_index % 26
                encrypted_text += alphabet[new_index]
        print(f"The encrypted text is: {encrypted_text}")


# Decrypt
#TODO-1: Create a different function called 'decrypt' 
# that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'decrypt' function, shift each letter 
# of the 'text' *backwards* in the alphabet by the shift 
# amount and print the decrypted text.  

def decrypt(a_text, a_shift):
    decrypted_text = ""
    for letter in text:
        index = alphabet.index(letter)
        new_index = index - shift
        decrypted_text += alphabet[new_index]
    print(f"The decoded text is : {decrypted_text}") 



#TODO-3: Check if the user wanted to encrypt or decrypt 
# the message by checking the 'direction' variable. 
# Then call the correct function based on that 'drection' 
# variable. You should be able to test the code to encrypt *AND* 
# decrypt a message.

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)


