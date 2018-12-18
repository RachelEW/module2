# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:36:16 2018

@author: winkl
"""

from random import randint

################################
"""Biased Dice Guessing Game"""
################################

def playGame():
    print("""Welcome to The Dice Game.
I will roll two dice and add the numbers together.
You must guess whether the sum of the numbers I roll will be odd or even!
If you ever want to end the game just write 'quit'.""")
    guess = 0
    oddCount = 0
    evenCount =  0
    gamesCount = 0
    while guess != "quit":
#adding count for odd and even numbers
        guess = input("Choose either 'odd', 'even' or 'quit'.\n")
        if guess == "odd":
            oddCount += 1
        elif guess == "even":
            evenCount += 1
        else:
            continue 
        gamesCount += 1
#main game
        number = rollingTwoDice()
#        print("Original Number:",number)
##################Printing Counts###################
#        print("\nOdd: ",oddCount)
#        print("Even: ",evenCount)
#        print("Number of Games: ",gamesCount)
####################################################
        if oddCount > 5 or evenCount > 5:
            if guess == "odd":
                oddBias = biasResultodd(oddCount, gamesCount, number)
                if oddBias:
#                    print("Bias against Odd")
                    number = biasDiceRollOdd(number)
#                    print("New number:",number)
            elif guess == "even":
                    evenBias = biasResulteven(evenCount, gamesCount, number)
                    if evenBias:
#                        print("Bias against even")
                        number = biasDiceRollEven(number)
#                        print("New number:",number)
        if number % 2 == 0 and guess == "even":
            print("\nCorrect! The sum of the numbers I rolled was",number,"which is even.")
        elif number % 2 != 0 and guess == "odd":
            print("\nCorrect! The sum of the numbers I rolled was",number,"which is odd.")
        elif guess == "quit":
            print("\nYou have choosen to exit the game.")
            break
        else:
            print("\nIncorrect, the sum of the numbers I rolled was",number,"and your guess was",guess,"- better luck next time!")
#counts
            
    print("\nGAME OVER: Thanks for playing!")

def rollingTwoDice():
    diceRoll = randint(1, 6)
    diceRoll2 = randint(1, 6)
    number = diceRoll + diceRoll2
    return number
    
def biasResultodd(oddCount, gamesCount, number):
        frequencyodd = oddCount / gamesCount
        if frequencyodd >= 0.70:
            return True
        else:
            return False

def biasResulteven(evenCount, gamesCount, number):
    frequencyeven = evenCount / gamesCount
    if frequencyeven >= 0.70:
        return True
    else:
        return False

def biasDiceRollOdd(number):
    while number % 2 != 0:
        number = rollingTwoDice()
    return number

def biasDiceRollEven(number):
    while number % 2 == 0:
        number = rollingTwoDice()
    return number

###TEST###
playGame()