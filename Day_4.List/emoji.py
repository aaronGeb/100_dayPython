#!/usr/bin/python3
"""
Write a program which mark a spot with an X.
the map is made 3x3 
[' 🐊 ',' 🐊 ',' 🐊 ']
[' 🐊 ',' 🐊 ',' 🐊 ']
[' 🐊 ',' 🐊 ',' 🐊 ']
The program should allow you to enter the position ot the list using two digit system 
the first digit is the row and the second digit is the column.
"""

row_1 =   [' 🐊 ',' 🐊 ',' 🐊 ']
row_2 = [' 🐊 ',' 🐊 ',' 🐊 ']
row_3 = [' 🐊 ',' 🐊 ',' 🐊 ']
map =[row_1,row_2,row_3]
#print("{}\n{}\n{}\n".format(row_1,row_2,row_3))
row_column = (input("Enter the row and column:\n"))
row = int(row_column[0])
column = int(row_column[1])
for i in range(len(map)):
    for j in range(len(map[i])):
        if i==row and j==column:
            map[i][j]='X'
        print(map[i][j],end=" ")
    print()    

