#!/usr/bin/python3
"""
Write a program that calculate the average student height from a list of height 
Don't use the sum() function
"""
student_heights =input("Input a list of students height:\n").split( )
for n in range(len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)   
list_size =len(student_heights) 
sum_height =0
for i in student_heights:
    sum_height +=i

average_height= sum_height/list_size
print("The average height of the student's are :{}".format(average_height))
