#!/usr/bin/python3
"""
Write a program that calculate the sum of all the even number from 1-100 include 100
dont ise the sum() function.
"""
even_sum=0
for i in range(2,101,2):
    even_sum +=i
print(even_sum)    