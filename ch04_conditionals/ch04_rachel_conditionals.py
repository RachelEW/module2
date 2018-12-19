# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:58:59 2018

@author: 612383461
"""

######################
"""Conditionals"""
######################

#--------------------------------------#
"""Task Two: Testing Boolean Example"""
#--------------------------------------#

age = 15
isaTeen = age >= 13 and age <=19
print(isaTeen)

age = 22
isaTeen = age >= 13 and age <= 19
print(isaTeen)

#------------------------------#
"""Task Three: IF statements"""
#------------------------------#

number = input("Enter a number between 1 and 10: ")
number = int(number) #converts the input string into an integer
if number > 10:
    print ("Too high!")    
if number <= 0:
    print ("Too low!")

#-------------------------------#
"""Task Four: ELSE statements"""
#-------------------------------#

#Adding an else statement

number = input("Enter a number between 1 and 10: ")
number = int(number) #converts the input string into an integer
if number > 10:
    print ("Too high!")    
elif number <= 0:
    print ("Too low!")  
else:
    print ("Just right!")

#---------------------------------#
"""Task Five: ELIF statements"""
#---------------------------------#

age = input("Enter an age: ")
age = int(age) #converts the input string into an integer
if age < 13:
   print("child")
elif age <18:
    print("teen")
elif age < 65:
    print("adult")
else:
    print("pensioner")

#NB: Order is important, stops at the first if/elif statement the value satisfies