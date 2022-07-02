#!/usr/bin/python3
""" A painting wall .
Instruction on the paint can says that 1- can can cover 5/m2 of wall
Give a random height and width calculate how many cans of paint you'll need to buy

"""
import math as m
def can_value(height, width,can_cover):
    return (height*width)/can_cover


wall_height = int(input("Enter the wall height:"))
wall_width = int(input("Enter the wall width:"))
can_cover = int(input("Enter the can covering area:"))
number_can_need = m.ceil(can_value(wall_height,wall_width,can_cover))
print("You need {} number of can".format(number_can_need))
