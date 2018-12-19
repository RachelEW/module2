# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:38:48 2018

@author: 612383461
"""
########################################
"""Operations, Strings and Variables"""
########################################

#Chapter 2 Exercises

#----------------------------------#
"""Task One: Simple Operations"""
#----------------------------------#

print (5-6)
print (8*9)
print (6/2)
print (5/2)
print (5.0/2)
print (5%2)
print (2*(10+3))
print (2**4)

#--------------------------------#
"""Task Two: Variable Practice"""
#--------------------------------#

age = 5
age = "almost three"
age = 29.5
age = "I really don't know"

a_longer_name = "hello, CFG!"

print (age)
print(type(age))
typeAge = type(age)
print(typeAge)

print (a_longer_name)
print (type("almost eight"))

#-------------------------------------------#
"""Task Three: Basic String Manipulation"""
#-------------------------------------------#

print ('hello' + 'world')
print ("Bob "*3)
print ("Bob" +"3")
print ("hello".upper())
print ("GOODBYE".lower())
print ("the lord of the rings".title())

#------More In Class Practice------#

print("Joke"*3)
print("Chen" + str(3))
print("hello".upper()) #This converts the string to uppercase
print("GOODBYE".lower())
print("the lord of the rings".title())
print(("Bob \n") * 3)

s1='hello'+'world' #This creates a variable
s2="Joke "*3 #This prints the string three times
s3=str(5)

print(s1+s2*10)
print(s1+s2+s3)

s1='4'
s2='8'
s3=2
result=int(s1)+int(s2)+s3
print(result)

strExample = 'a,b,c,d,happy'

SplitStr=strExample.split(',')
print(SplitStr)

#------------------------------#
"""Task Four: Formatting"""
#------------------------------#

age=5
hobby='painting'

age_description="I am {} years old and I enjoy {}.".format(age,hobby)
print(age_description)

age_description2="My age is {0} and I like {1}.".format(age,hobby)
print(age_description2)

#------More in Class Practice------#

#Testing using three quotation marks to allow comments to cross several lines
test="""Here is a first line
This is a second line
The third line is here"""
print(test)

#-------------------#
"""Homework Task"""
#-------------------#

print(10/3)
print(10%3)

a = 1
a = a+1
print (a)
b = "hello"
print (b)
c = b.title()
print (b)
print (c)
d = "hello"
e = d.title()
print (d)
print (e)
name = "Dave"
f = "Hello {0}! ".format(name)
print (f)
name = "Sarah"
print (f)
print (f*5)