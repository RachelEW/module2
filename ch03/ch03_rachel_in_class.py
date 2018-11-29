# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:54:55 2018

@author: 612383461
"""

#print ("What's your name?")
#name = input()
#
#print ("Hello {}!".format((name).upper()))
#
##The first option gives a space between the question and where you type
#
#name = input("What's your name? ").title()
#print ("Hello {}!".format(name.upper()))

#The second option gives the input o the same line as the question

#print ("Where are you from?")
#hometown = input()
#
#print ("Oooh, I loved {} when I visited!".format((hometown).title()))
#
#print ("How old are you?")
#age = input()
#
#print ("{} is a great age, {}!".format(age, (name.title())))
#
#print ("What colour are your socks?")
#socks = input().title()
#
#print ("{}, I like your sense of style, {}.".format(socks,name))

def hello_world():
    print ("Hello World!")
    
hello_world()

def my_name():
    print ("Rachel Winkler")
    print (2+2)
    
my_name()

def write_name():
    print ("What is your name?")
    name = input().title()
    print ("Your name is {}".format(name))
    
write_name()

def hello_world():
    print ("Hello World!")
    write_name()
    
hello_world()

def adding_numbers():
    print ("Choose a number")
    number_one = input()
    print ("Choose a second number")
    number_two = input()
    result = float(number_one)+float(number_two)
    print ("The sum of the numbers you chose is {}.".format(result))
    
adding_numbers()

def hello_world():
     print ("Hello World!")
     write_name()
     adding_numbers()
     
hello_world()