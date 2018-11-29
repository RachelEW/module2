# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:34:14 2018

@author: 612383461
"""

#In Class Exercises

print (5-6)
print (8*9)
print(6/2)
print(5/2)
print(5.0/2)
print(5%2)
print(2*(10+3))
print(2**4)

age = 5
age = "almost three"
age = 29.5
age = "I really don't know"
print(age)

print(type(age))
typeAge = type(age)
print(typeAge)

print("hello" + "world")

print("Joke"*3)
print("Chen" + str(3))
print("hello".upper())
print("GOODBYE".lower())
print("the lord of the rings".title())
print(("Bob \n") * 3)

s1='hello'+'world'
s2="Joke "*3
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

age=6
hobby='dancing'

age_description="I am {} years old and I like {}.".format(age,hobby)
print(age_description)

age_description2="My age is {0} and I enjoy {1}.".format(age,hobby)
print(age_description2)

test="""Here is a first line
This is a second line
The third line is here"""
print(test)