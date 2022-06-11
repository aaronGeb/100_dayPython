#!/usr/bin/python3
"""
Bill calculator 
"""
print("Welcome to the tip calculator.")
total_amount =eval(input("What was the total bill? $"))
tip_waiter =eval(input("What percentage tip would you like to give? 10, 12, or 15?"))
number_of_people =eval(input("how many people to split the bill?"))
sum_total = total_amount+total_amount*tip_waiter*0.01
total_bill =round(((total_amount+total_amount*(tip_waiter/100))/number_of_people),2)
print("The bill is {} and the tip percent is {} % so,the total bill is {} and we share it with {} and each pays {:.2f} dollar ".format(total_amount,tip_waiter,sum_total,number_of_people,total_bill))
