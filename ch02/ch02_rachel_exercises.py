# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:38:48 2018

@author: 612383461
"""

#Chapter 2 Exercises

print (5-6)
print (8*9)
print (6/2)
print (5/2)
print (5.0/2)
print (5%2)
print (2*(10+3))
print (2**4)

age = 5
age = "almost three"
a_longer_name = "hello, CFG!"
print (age)
print (a_longer_name)
print (type("almost eight"))
print ('hello' + 'world')

print ("Bob "*3)
print ("Bob" +"3")
print ("hello".upper())
print ("GOODBYE".lower())
print ("the lord of the rings".title())

#Homework

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

print ("Hello World!")
print ("Hello Again")
print ("I like typing this.")
print ("This is fun.")
print ('Yay! Printing.')
print ("I'd much rather you 'not'.")
print ('I "said" do not touch this.')

#A comment, this is so you can read your program later.
#Anything after the # is ignored by python.
print ("I could have code like this.") # and the comment after is ignored
#You can also use a comment to "disable" or a comment out a piece of code:
#print "this won't run."
print ("This will run.")

print ("I will now count my chicken:")

print ("Hens", 25+30/6)
print ("Roosters", 100-25*3%4)

print ("Now I will count the eggs:")
      
print (3_2_1-5+4%2-1/4+6)

print ("Is it true that 3+2<5-7?")

print (3+2<5-7)

print ("what is 3+2?",3+2)
print ("What is 5-7?", 5-7)
print ("Oh, that's why it's False.")

print ("How about some more.")

print ("Is it greater", 5>-2)
print ("Is it greater or equal?", 5>=-2)
print ("Is it less or equal?", 5<=-2)

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars available")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car")