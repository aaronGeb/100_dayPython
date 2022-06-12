#!/usr/bin/python3
"""
Write a program which will select a random name from a list 
of names.The person selected will have to pay for everybody's food bill
"""
import random as ra

names_string = input("Give me everybody's names separated by comma:\n")
name = names_string.split(",")
rand_num = ra.randint(0,(len(name)-1))
print(name[rand_num])