#!/usr/bin/python3
import string as s
from turtle import position

a =s.ascii_lowercase
alphabet =list(a)
direction = input("Type the 'encode' to encrypt, type  'decode' to decrypt:\n") 
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))
#TOD-1: Create a function call 'encrypt' that takes the 'text' and 'shift' as inputs.
"""TOD-2: Inside the 'encrypt' function ,shift each letter of the 'text' forward in the alphabet by the amount and print the 
     encrypted text.
     eg.
      #plain_text ="hello"
      #shift 5
      #cipher_text = "mjqqt"
      #print output: "The encoded text is "mjqqt"
     """
"""TOD-3:Check if the user wanted to encrypt  ot decrypt the message by checking the 'direction'
          variable .Then  call the correct function based on that 'direction' variable.You should be able to 
          test the code encrypt **AND** decrypt a message.
"""     
#solution-1&2
def encrypt(plain_text,shift_amount):
    cipher_text =""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position +shift_amount
        new_letter = alphabet[new_position]
        cipher_text +=new_letter
    print("The encode text is: {}".format(cipher_text))
#Solution 3
def decrypt(cipher_text,shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position  = alphabet.index(letter)
        new_position =position -shift_amount
        plain_text +=alphabet[new_position]
    print("The decode text is:{}".format(plain_text))    


if direction == 'encode':
    encrypt(text,shift)
elif direction == 'decode':
     decrypt(text,shift)
#TOD-1 : Combine the encrypt() and decrypt() function in to one 
# single function called caesar()



def caesar(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
            shift_amount *=-1
    for letter in start_text:
        position = alphabet.index(letter)  
        
        new_position = position + shift_amount
        end_text +=alphabet[new_position]  
    print("The {cipher_direction}d text is:{]".format(end_text))    



