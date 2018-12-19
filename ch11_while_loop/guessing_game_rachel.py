# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:57:36 2018

@author: winkl
"""

from random import randint

def guess(attempts, amount):
    number = randint(1, amount)
    print("Welcome! Can you guess the secret number?")
    while attempts > 0:
        print("You have ", attempts, " guesses remaining. The number is between 0 and", amount,".")
        guess = input("Make a guess: ")
        guess = int(guess)
        if guess == number:
            print("Well done! Your guess was correct!")
            break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")
        attempts -= 1
    if attempts == 0:
        print("You have no guesses remaining, the secret number was", number,"better luck next time!")
        print("GAME-OVER: Thank you for playing!")
    else:
        print("GAME-OVER: Thank you for playing!")

###TEST###
guess(4,25)