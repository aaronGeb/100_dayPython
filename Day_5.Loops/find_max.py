#!/usr/bin/python3
"""
Write a program that calculate the hightest Score from a list of scores
Don't use the max() function.
"""
student_score = input("Input a list of student:\n").split( )
for i in range(len(student_score)):
    student_score[i]=int(student_score[i])
max =0
for k in student_score:
    if k>max:
        max=k
print("The highest score in the class is:{}".format(max))  
