# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:14:36 2018

@author: 612383461
"""

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
