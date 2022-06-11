#!/usr/bin/python3
""" I was reading this article by Tim Urban -your Life in Weeks 
     and realized just how little time we actually have

Create a programme using maths amd f-String that tells us hoe many days,
weeks months we have left if we live until 90 years old
It will take your current age as the input and output a message with our time left in.
x days,y weeks,z months left
"""
age = eval(input("Enter your age\n"))
years_remaining =90-age
day_remaining = years_remaining*365
week_remaining =years_remaining*52
month_remaining =years_remaining *12
print("You have {} days, {} weeks and {} month left".format(day_remaining,week_remaining,month_remaining))


