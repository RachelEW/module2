# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:22:45 2018

@author: winkl
"""

######################
"""While Loops"""
######################

#------------------------------#
"""Task One: Repeat division"""
#------------------------------#

x = 33
while x >= 1:
    print(x, ': ', end='') #end='' adds a space at the end
    x = x / 2
print(x)

#-------------------------------------------#
"""Task Two: Computing triangular numbers"""
#-------------------------------------------#

def generateTriangularNo(n):
    triangularSum = 0
    while n >= 1:
        triangularSum = triangularSum + n
        n = n-1
    return(triangularSum)
    
#triangularSum1 = generateTriangularNo(4)
#print(triangularSum1)

#--------------------------------------------------------------#
"""Task Three: Determining if a student has passed or failed"""
#--------------------------------------------------------------#
def generateGrade():
    counter = 0
    mark = 0
    averageMark = 0
    while counter < 6:
        mark = input("What mark did the student achieve in the test? ")
        mark = int(mark)
        counter += 1
        averageMark = (averageMark + mark) / 2
        if averageMark >= 70:
            print("Grade: First Class")
        elif averageMark >= 40:
            print("Grade: Pass")
        else:
            print("Grade: Fail")
    print("Average Mark: ", averageMark)

###TEST###
#generateGrade()

#------------------------------------------------------------#
"""Task Four: Using a break statement to exit a while loop"""
#------------------------------------------------------------#

i = 55
while i > 10:
    print(i)
    i = i*0.
    if i == 35.2:
        break

#-----------------------------------------------------#
"""Additional Exercise: Greeting until user is done"""
#-----------------------------------------------------#

def greet():
    name = input("What is your name? ")
    while name != "done":
        print("Hello,", name, "nice to meet you!")
        name = input("""What is your name?
Or print 'done' if you would like to exit the greeting generator. """)
    print("Thank you for using the greeting generator. Goodbye.")
    
###TEST###
#greet()

#OR an alternative...#

def greet2():
    while True:
        name = input("Enter name: ")
        if name == "done":
            break
        print("Hello", name)
        
###TEST###
#greet2()
        
#----------------------------------------------#
"""Task Five and Six: Design a Guessing Game"""
#----------------------------------------------#

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