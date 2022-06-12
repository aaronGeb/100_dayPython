#!/usr/bin/python3
"""
Write a program that works out whether if a given year is a leap year .
A normal year has 365 ,leap year have 366 with an extra day in February.
"""
num_year= eval(input("Enter the year\n"))
if num_year %4==0:
    if num_year %100==0:
        if num_year %4==0:
         print("{},is a leap year".format(num_year))
else:
    print("{},is not leap year".format(num_year))    
