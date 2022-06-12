#!/usr/bin/python3
"""
Congratulation ,you've git a job at python pizza. 
Your first job is to build an automatic pizza order program.
"""
print("Welcome to Python Pizza Deliveries:")
pizza_size = input("Select Pizza size please? S,M,L\n")
add_pepperoni =input("Do you want pepperoni? Y, N\n")
extra_cheese =input("Do you want extra cheese? Y, N\n")

bill =0
if pizza_size == 'S':
    bill +=15
    if add_pepperoni =='Y':
       bill +=2
    if extra_cheese == 'Y':
        bill +=1 
elif pizza_size =='M' :
    bill +=20
    if add_pepperoni =='Y':
       bill +=3
    if extra_cheese == 'Y':
        bill +=1 
elif pizza_size == 'L':
    bill =25
    if add_pepperoni =='Y':
       bill +=3
    if extra_cheese == 'Y':
        bill +=1 
print("Your final bill is: ${}".format(bill))        
    
