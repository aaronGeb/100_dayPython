#!/usr/bin/python3
""" Write a programme that calculate the Body Mass index (BMI)
from a yser weight and height
BMI = weight(Kg)/height^2(m^2)

"""
height_meter= eval(input("Enter your height in meter(M)\n"))
weight_kilogram = eval(input("Enter yoy weight in (kg)\n"))
bmi = int((weight_kilogram)//((height_meter**2)))
print("Your body mass index is:",bmi)