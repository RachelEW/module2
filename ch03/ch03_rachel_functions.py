## -*- coding: utf-8 -*-
#"""
#Created on Mon Dec  3 09:43:32 2018
#
#@author: winkl
#"""
#
def hello_world_2args(a, b):
    print ("{} {}".format(a,b))
    
a1 = 'hello'
b1 = 'world'
a2 = 'love'
b2 = 'coding'
#hello_world_2args(a1, b1)
#hello_world_2args(a2, b2)

def hello_world_4args(a, b, c, d):
    print ("{} {} {} {}".format(a,b,c,d))

a3 = "Dogs"
b3 = "are"
c3 = "the"
d3 = "best!"

#hello_world_4args(a3, b3, c3, d3)

def hello_world_3args(a, b, c,):
    print (a, b, c)
    
a4 = "Dogs"
b4 = "are"
c4 = "great"

#hello_world_3args(a4, b4, c4)

#print (list(range (10)))
#print (list(range (1,10)))
#print (list(range (1,10,2))) #third value is the step size

def add_two_numbers_from_args(number1, number2): #These can only be variable names
    answer = number1 + number2
    print ("{} plus {} is {}".format(number1, number2, answer)) #variables are then defined outside the function

num1 = 5
num2 = 10

#add_two_numbers_from_args(num1,num2) #inside the brackets tell the function which variables you are calling

def convert_distance_print(miles):
    kilometers = (miles * 8.0) / 5.0
    print ("Converting distance in miles to kilometers:")
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers)
    
def convert_distance(miles):
    kilometers = (miles * 8.0) / 5.0
    return miles, kilometers

#returned_value1 = convert_distance(35)
#print (returned_value1, "\n")


#inside the brackets tell the function which variables you are calling

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

#temp_London = convert_temperature(12)
#print (temp_London)