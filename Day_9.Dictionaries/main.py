#!/usr/bin/python3

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for grade in student_scores:
    if 91 < student_scores[grade] < 100:
        student_grades[grade] = 'Outstanding'
    elif 81 <= student_scores[grade] <= 90:
        student_grades[grade] = 'Exceptional'
    elif 71 < student_scores[grade] < 80:
        student_grades[grade] = 'Accepted'
    else:
        student_grades[grade] = 'Failed'


# 🚨 Don't change the code below 👇
print(student_grades)
