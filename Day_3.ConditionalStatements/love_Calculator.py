#!/usr/bin/python3
"""
Write a program that test the compatibility between two people 
We're going to use the super scientific method recommended by BuzzFeed.
"""
from itertools import count


print("Welcome to the Love Calculator!")
first_name =input("Enter your name ,please\n")
second_name =input("Enter your name ,please\n")
first_name_lowe_case=first_name.lower()
second_name_lower_case = second_name.lower()
combined_string =first_name_lowe_case+second_name_lower_case
count =0
look_var = 'true'.lower()
for i in look_var:
    for j in combined_string:
        if i==j:
            count +=1

love_var = 'love'.lower()
yCount=0
for i in love_var:
    for j in combined_string:
        if i==j:
            yCount +=1

love_score =int(str(count)   + str(yCount) )
 
if love_score < 10 or love_score > 90:
    print("Your Score is {}, you got together like coke and mentos.".format(love_score))
elif 40 <love_score<50:
     print("Your Score is {}, you got together".format(love_score))






    