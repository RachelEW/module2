# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:28:12 2018

@author: winkl
"""

###############################
"""OOP Project Introduction""" 
###############################

#------------------------------------------------------------#
"""Task One, two, three, four: Initialise the person class"""
#------------------------------------------------------------#

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        if gender == 'm':
            self.isMale = True
        elif gender == 'f':
            self.isMale = False
        else:
            print('Gender not recognised')
            
    def greetingInformal(self):
        print('Hi', self.name)
        
    def greetingFormal(self):
        if self.isMale:
            print('Welcome, Mr ', self.name)
        else:
            print('Welcome, Ms ', self.name)
            
    def greetingAgeBased(self):
        if self.age < 18:
            print('Welcome, young ', self.name)
        elif self.age > 60:
            print('Welcome, venerable ', self.name)
        else:
            self.greetingFormal()

class Wizard(Person):
    def greetingFormal(self):
        print('Welcome, Mr ', self.name, end=' ')
        print('- you\'re a fine wizard!')

###TESTING###
p1 = Person('John', 62, 'm')
p2 = Person('Jean', 12, 'f')
p1.greetingInformal()
p1.greetingFormal()
p2.greetingFormal()
p1.greetingAgeBased()
p2.greetingAgeBased()

p3 = Wizard('Harry', 12, 'm')
p3.greetingFormal()
