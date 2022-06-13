#!/usr/bin/python3
"""

"""
import string as st
import random as ra
number_list =list(st.digits)
letter_list=list(st.ascii_letters)
pun_list = list(st.punctuation)
print("Welcome to the PyPassword Generator")
letter_password =eval(input("How many letter would you like in your password?\n"))
symbol_password =eval(input("How many symbol would you like in your password?\n"))
number_password=eval(input("How many digits would you like in your password?\n"))
password_list =[]
for i in range(letter_password):
    password_list +=ra.choice(letter_list)

for k in range(symbol_password):
    password_list +=ra.choice(pun_list)
for j in range(number_password) :
    password_list +=ra.choice(number_list)  

print(password_list)
ra.shuffle(password_list)
password =''
for char in password_list:
    password +=char

print("The generated password :{}".format(password))    