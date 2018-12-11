# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:48:21 2018

@author: Cheye
"""
import random
def guessno():
    numberofGuesses = 0
    number = random.randint(1,50)
    
    name = input("Hello! What is your name? ")
    
    print(name + ", I am thinking of a whole number between 1 and 50. Can you guess what it is?")
    
    while numberofGuesses < 8:
      guess = int(input("Take a guess "))
    
      numberofGuesses = numberofGuesses + 1;
      guessesLeft = 8 - numberofGuesses;
    
      if guess < number:
        guessesLeft=str(guessesLeft)
        print("Your guess is too low! You have " + guessesLeft + " guesses left")
    
      if guess > number:
        guessesLeft=str(guessesLeft)
        print("Your guess is too high! You have " + guessesLeft + " guesses left")
    
      if guess==number:
        break
    
    if guess==number:
      numberofGuesses=str(numberofGuesses)
      print("Good job! You guessed the number in " + numberofGuesses + " tries :)")
    
    if guess!=number:
      number=str(number)
      print("Sorry. The number I was thinking of was " + number + " :)")
guessno()
## Ask Player if he/she wants to continue playing
second_guess = (input("Would you like to continue playing? Y/N " ))
while second_guess == str('Y'):
    guessno()
    second_guess = (input("Would you like to continue playing again? Y/N" ))
else:
    print(input("Press any key to exit"))
    

