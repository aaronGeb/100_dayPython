#!/usr/bin/python3
"""
Write a program that interprets the BMI based on user weight and height
Based on BMI values
.under 18.5 are underweight
.Over 18.5 but below 25 they have a normal weight
.Over 25 but below 30 they are overweight
.over 30 but below 35 they are obese
.Above 35 they are clinically obese
"""
height_meter= eval(input("Enter your height in meter(M)\n"))
weight_kilogram = eval(input("Enter yoy weight in (kg)\n"))
bmi = int((weight_kilogram)//((height_meter**2)))
if bmi < 18.5:
    print("Your underweight")
elif 18.5 <=bmi<25:
    print("Your normal weight")
elif  25<bmi <30:
    print("Your Overweight")   
elif 30<bmi <35:
    print("Your Obese")
else:
    print("Your are Clinically Obese")        
