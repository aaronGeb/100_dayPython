#!/usr/bin/python3
"""
#step-1
   word_list =['ardvark','baboon','camel']
   #TODO-1 -Randomly choose a word from the word_list ans assign it to a variable called chosen_word
     

    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess .Make guess lower letter
   #TODO-3- Check if the letter the user guessed (guess) is one of the letter in thr chosen_word.
#step-2
     #TODO-1 - create an empty list called display
     # for each letter in the chosen_world ,add a "_"to 'display'
     # So if the chosen_word was "apple",display should be ["_","_","_","_","_"] with 5 "_" representing each letter to guess 
     #TODO-2:- Loop through each position in the chosen_word;
      # if the letter at the position matches 'guess' then reveal that letter in the display at that position.
      # e.g .If the user guessed 'p' and the chosen word was 'apple',then display should be ['_','p','p','_','_'].
      #TODO-3: - print 'display' and you should see the guessed letter int the correct position and every other letter replace '_'
#step-3
       #TODo-1: - Use a while loop to let the user guess again .THe loop should only stop once the user has guessed all the letter in the 
                 chosen_word nd 'display' has no more blanks ("_").Then you can tell the user they've won
"""
import random as ra
word_list = ['aardvark','baboon','camel']

chosen_word=ra.choice(word_list)
#Testing the code 
print(chosen_word)
correct_guess =0
new_list=[]
count =0
while count< len(chosen_word):
    guess =  input("Guess a letter:").lower()
    for letter in range(len(chosen_word)):
        if guess==letter:
            correct_guess +=1
            new_list +=letter
        elif len(new_list) > len(chosen_word) :
            pass 
        else:
            new_list +='_'

   # print(new_list)
  

    count +=1 
print(new_list)
#new_list=new_list.remove('_')  
print("The chosen word is:{}".format(chosen_word))    
if correct_guess == len(chosen_word):
    print("You'r guess letters are:{}".format(new_list))
    print("Congratulation You won!") 

else:
    print("You'r guess letters are:{}".format(new_list))
    print("Try agin please!") 