# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:36:16 2018

@author: winkl
"""

from random import randint

#############################
"""Dice Guessing Game"""
#############################

def playGame():
    print("""Welcome to The Dice Game.
I will roll two dice and add the numbers together.
You must guess whether the sum of the numbers I roll will be odd or an even!
If you ever want to end the game just write 'quit'.""")
    guess = 0
    while guess != "quit":
        guess = input("Choose either 'odd', 'even' or 'quit'.\n")
        diceRoll = randint(1, 6)
        diceRoll2 = randint(1, 6)
        number = diceRoll + diceRoll2
        if number % 2 == 0 and guess == "even":
            print("\nCorrect! The sum of the numbers I rolled was",number,"which is even.")
        elif number % 2 != 0 and guess == "odd":
            print("\nCorrect! The sum of the numbers I rolled was",number,"which is odd.")
        elif guess == "quit":
            print("\nYou have choosen to exit the game.")
            break
        else:
            print("\nIncorrect, the sum of the numbers I rolled was",number,"and your guess was",guess,"- better luck next time!")
    print("\nGAME OVER: Thanks for playing!")
    
###TEST###
playGame()