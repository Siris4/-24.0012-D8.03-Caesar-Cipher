#if you go through the top 4 lines (4-7) and press Ctrl+/ on all  4, you can invert the code and trouble shoot which directory it's based in, for the
#Environment PATH


# import sys
# print(sys.path)
from __2x__caesar_cipher_logo_230929 import logo    # you DON'T place .py at the end of the file location name :)
print(logo)

#Directory PATH location: C:\Users\guber\Desktop\CoDex - Code Index - GitHub for HDD\Python\100 Days of Code PyCharm Code




#Encryption:
'''
    def encrypt(plain_text, shift_amount):  # keep the parameter and argument names will help a lot!
        cipher_text = ""  # this is equivalent of counter = 0, but in letters!! you are adding the discovered shifted letter, and just adding this to the blank string
        for letter in plain_text:
            position = alphabet.index(letter)  # .index() was the missing piece to determining which location that something is in.
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encoded text is {cipher_text}")
'''



        #you get to define the function and also what variables and how many get injected into the fucntion
def caesar(direction, text, shift): # Examples to inject in function: (encode, jesus, 6)
    caesar_text = ""
    new_shift = shift % 26         #no need for global variable. You can assign the math here,
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if shift > 26:
                new_shift = shift % 26
            if direction == "encode":
                new_position = position + new_shift
            elif direction == "decode":
                new_position = position - new_shift
            newest_letter = alphabet[new_position]
            caesar_text += newest_letter
        else:
            caesar_text += letter

    print(f"The {direction}d text is {caesar_text}")


while True:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    caesar(direction, text, shift)

    i = input(f"Do you want to play again? (Y or N): ").upper()
    if i != "Y":
        break

#Decryption:
'''
    def decrypt(encoded_text, encoded_shift_amount):
        decrypted_text = ""
        for letter in encoded_text:
            position = alphabet.index(letter)
            new_position = position - encoded_shift_amount
            new2_letter = alphabet[new_position]
            decrypted_text += new2_letter
        print(f"The decrypted text is {decrypted_text}")
'''





'''
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(encoded_text=text, encoded_shift_amount=shift)

i = input(print(f" Do you want to crypt anything else? (Y or N) "))
'''

# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.


# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# e.g.
# cipher_text = "mjqqt"
# shift = 5
# plain_text = "hello"
# print output: "The decoded text is hello"


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.


'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    position = alphabet.index(char)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
'''