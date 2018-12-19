# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:54:55 2018

@author: 612383461
"""

#####################
"""Functions"""
#####################

#---------------------------------------------------#
"""Task One and In Class Practice with User Input"""
#---------------------------------------------------#

#Another option for user input:
#name = input("What's your name? ").title()
#print ("Hello {}!".format(name.upper())) #The first option gives the input o the same line as the question

def conversing_with_user():
    print ("What's your name?")
    name = input()
    print ("Hello {}!".format((name).upper())) #The second option gives a space between the question and where you type
    print ("Where are you from?")
    hometown = input()
    print ("Oooh, I loved {} when I visited!".format((hometown).title()))
    print ("How old are you?")
    age = input()
    print ("{} is a great age, {}!".format(age, (name.title())))
    print ("What colour are your socks?")
    socks = input().title()
    print ("{}, I like your sense of style, {}.".format(socks,name))

#----------------------------------#
"""Task Two: Creating Functions"""
#----------------------------------#

def hello_world():
    print ("Hello World!")
    
def my_name():
    print ("Rachel Winkler")
    print (2+2)

#--------------------------------------------#
"""Task Three: Using Range with Arguments"""
#--------------------------------------------#

def printing_list_using_range():
    print (list(range (10)))
    print (list(range (1,10)))
    print (list(range (1,10,2))) #third value is the step size

#-------------------------------------------------------------------#
"""In Class Practice: Calling a Function within another Function"""
#-------------------------------------------------------------------#

def write_name():
    print ("What is your name?")
    name = input().title()
    print ("Your name is {}".format(name))
    
def hello_world2():
    print ("Hello World!")
    write_name()
    
def adding_numbers():
    print ("Choose a number")
    number_one = input()
    print ("Choose a second number")
    number_two = input()
    result = float(number_one)+float(number_two)
    print ("The sum of the numbers you choose is {}.".format(result))

def hello_world3():
     print ("Hello World!")
     write_name()
     adding_numbers()

#----------------------------------------------------------#
"""Task Three Continued: Adding Numbers using Arguments"""
#----------------------------------------------------------#

def add_two_numbers_from_args(number1, number2): #These can only be variable names
    answer = number1 + number2
    print ("{} plus {} is {}".format(number1, number2, answer)) #variables are then defined outside the function

#-------------------------------------------------#
"""In Class Practice: Functions with arguements"""
#-------------------------------------------------#

def hello_world_2args(a, b):
    print ("{} {}".format(a,b))

def hello_world_4args(a, b, c, d):
    print ("{} {} {} {}".format(a,b,c,d))

def hello_world_3args(a, b, c,):
    print (a, b, c)

#----------------------------------------------#
"""Mid-Class Challenge: Distance Conversion"""
#----------------------------------------------#

def convert_distance_print(miles):
    kilometers = (miles * 8.0) / 5.0
    print ("Converting distance in miles to kilometers:")
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers)
    
#Returning the value insead of printing
    
def convert_distance(miles):
    kilometers = (miles * 8.0) / 5.0
    return miles, kilometers
    
#---------------------------------------#
"""Task Four: Temperature Conversion"""
#---------------------------------------#

def convert_temperature_print(centigrade):
    fahrenheit = centigrade * 9.0 / 5.0 + 32
    kelvin = centigrade + 273.15
    print ("Converting temperature in centigrade to fahrenheit and kelvin:")
    print ("Temperature in centigrade:", centigrade)
    print ("Temperature in fahrenheit:", fahrenheit)
    print ("Temperature in kelvin:", kelvin)
    
def convert_temperature(centigrade):
    fahrenheit = centigrade * 9.0 / 5.0 + 32
    kelvin = centigrade + 273.15
    return centigrade, fahrenheit, kelvin

#to print a returned value, assign a variable to a value and then we can do things with this variable such as print it
#returned_value2 = convert_temperature(20)
#print (returned_value2)
    
#--------------------------------#
"""Task Five: Return Value"""
#--------------------------------#

def add_two_numbers_and_return_value():
    number1 = 1
    number2 = 2
    answer = number1 + number2
    return answer