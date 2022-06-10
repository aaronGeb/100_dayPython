#!/usr/bin/python3
"""Swap to input values """
a= eval(input("Enter the first number :"))
b= eval(input("Enter the second number :"))
print("a =:",a)
print("b =:",b)
a, b = b,a
print("a =:",a)
print("b =:",b)