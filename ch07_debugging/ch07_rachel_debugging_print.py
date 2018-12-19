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