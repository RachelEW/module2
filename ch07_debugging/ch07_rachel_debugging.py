# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:20:09 2018

@author: winkl
"""

###############################################
"""Debugging Using Print to Check for Errors"""
###############################################

#Original code to debug:

userInput = input('please give a number ')
result = userInput - 2

#The original code gives a TypeError, therefore print the type of userInput to find out what the error is
#This shows userInput is a string
#To make it work convert userInput into an integer

userInput = input('please give a number ')
#print(type(userInput))
userInput = int(userInput)
result = userInput - 2

#Always remove debugging lines after!

################################################
"""Debugging using Python's Debugging System"""
################################################

userInput = input('please give a number ')

def simpleOperation(userInput):
    intInput = int(userInput)
    result = intInput - 2
    return result

def nestedOperation(result):
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2

result = simpleOperation(userInput)
result2 = nestedOperation(result)
print(result2)

#--------------------------------#
"""Python Debugging Mode Notes"""
#--------------------------------#

#Use blue buttons to enter debugging mode.
#The ﬁrst button starts running your code until the break point.
#The second button runs your code line-by-line until the breakpoint.
#The third button is for stepping into sections (class and functions).
#The fourth button is to step out of a section.
#The fifth button is to continue to the next breakpoint.
#The last button is to exit debugging mode.
