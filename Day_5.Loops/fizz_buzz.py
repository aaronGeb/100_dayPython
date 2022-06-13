#!/usr/bin/python3
"""
Write a program that automatically print the solution to the FIZZBuzz game
range from 1-100
"""
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz,{}".format(i))
    elif i%3==0:
        print("Fizz,{}".format(i))    
    elif i%5==0:
        print("Buzz,{}".format(i))    