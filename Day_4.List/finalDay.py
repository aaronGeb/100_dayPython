#!/usr/bin/python3
"""
"""
import random as ra
rock = '''
 
 
     .._                             wWWWw
 ,;//\\\                           www@-O\
  ((-.-\)                          www( o) O===-
 _))'=`(\-.                        wwW �(     \\
(          \                       w(  )_\     |\
| | .)(. |\ \                       |..)__|_/  |
| | /  \ | \ \                      |_______://|
| |/�(_)�\__\_\_____ ooo             )===&     |
(___\\\][] _|_|\\\|_|<<<}           ( :  |     |
  |\o*___(           ooo             |:  |     |
 :|       |:                         |:  |     |
 :|   Y   |:                         |:  |     |
 :|   |   |:                         |   )     |
                      MJP
 
 
 
 
 
 '''
paper = '''
 
 
       __                       __
         __\_\___               ___/_/__
 /_______ \___       ___/\_______\
           \_\  \/__/\_____/\__\/  /_/
                    \/_____\/                      __
                     \o | o/_____ ________________/\_\
                      \ | /_______\_______________\/
                       \_/        /  b'ger        |
                                 /\           _   |
                                / /\_________/ |__|
                               / /             / /
                              /_/             /_/
                              \ \             \ \
                               \ \             \_\
                                \_\            /_/
                                /_/            |_|
 
 
 
 
'''
scissors = '''



   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/


'''
game_list =[rock,paper,scissors]
computer_choose =ra.randint(0,2)
print("Welcome to the Rock ,paper and Scissors game:\n")
choice = eval(input("What do you choose? Type 0 for Rock,1 for paper or 2 for Scissor:\n"))
if choice<0 or choice >len(game_list):
  print("Invalid number choose,please try again! ")
else:  
  print(game_list[choice])
  print("computer choose:")
  print(game_list[computer_choose])

  if choice ==0 and  computer_choose==2:
     print("You win")
  elif computer_choose > choice:
    print("You lose")
  elif computer_choose==choice:
    print("It's draw")
  else:
    print("Invalid Number you lose")        