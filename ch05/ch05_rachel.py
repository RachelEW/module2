# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:08:33 2018

@author: 612383461
"""
import sys

#Task One

#class Customer(object):
#    """A customer of ABC Bank with a checking account. Customers have the following properties:
#        Attributes:
#            name: A string representing the customer's name.
#            balanca: A float tracking the current balance of the customer's account. """
#            
#    def __init__(self, name, balance=0.0):
#        """Return a Customre object whose name is *name* and starting balance is *balance*."""
#        self.name = name
#        self.balance = balance
#        
#    def withdraw(self, amount):
#        """Return the balance remaining after withdrawing *amount* dollars. """
#        if amount > self.balance:
#            raise RuntimeError('Amount greater than available balance.')
#        self.balance -= amount
#        return self.balance
#
##can write this as an else statement for self.balance but this isn't neccessary
#        
#    def deposit(self, amount):
#        """Return the balance remaining after depositing *amount* dollars."""
#        self.balance += amount
#        return self.balance
#    
## self is how the object refers to itself
#        #when you call __init__ method you never call init, you call it through the class (in this case Customer) then give the variables the equivalent values
#    
##Define a Customer by naming the Customer and defining the values of name and balance
##we can create as many custommrs as we want but there is only one customer class by whch customers are defined.
#        
#sarah = Customer('Sarah Smith', 1250)
#print(sarah.balance)
#print(sarah.name)
#sarah.withdraw(50)
##sarah is an object so you can call any function by writing .function() for the functions which are deifned for this type of object only
#sarah.withdraw(2000)
#sarah.deposit(25)
#sarah.deposit(1000)


#Task Two: Inheritance

class Animal(object):
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
#Don't need to use init because we don't need to define any variables for the methods we are using. Have added for practice.
        
    def eat(self):
        print('yum')

class Pet(Animal):
    def greet(self):
        print('runs to human')

class Dog(Pet):
    
    def __init__(self, name='Dog', age=0, treats=0):
        Animal.__init__(self, name, age=0)       
        self.treats = treats

    def bark(self):
        print('Woof!')
        
    def do_trick(self):
        print('How many treats do you want to give {}?'.format(self.name))
        TreatAmount = int(input())
        self.treats += TreatAmount
        
        if self.treats < 0:
            raise RuntimeError('Cannot have a negative number of treats!')
        elif self.treats >= 18:
            print('brings a toy')
        elif self.treats >= 12:
            print('rolls over')
        elif self.treats >= 8:
            print('spins in a circle')
        elif self.treats >= 4:
            print('lies down')
        else:
            print('sits')
        
class Cat(Pet):
    def __init__(self, name, age=0, NumberofStrokes=0):
        Animal.__init__(self, name, age=0)
        self.NumberofStrokes = NumberofStrokes
        
    def meow(self):
        print('Meow')
        
    def jump_on_human(self):
        print('How many times do you want to stroke {}?'.format(self.name))
        self.NumberofStrokes = int(input())
      
        if self.NumberofStrokes < 0:
            raise RuntimeError('Cannot stroke a cat a negative number of times!') 
        elif self.NumberofStrokes < 20:
            print('Purr '*self.NumberofStrokes)
        else:
            print('Purr'+('r'*self.NumberofStrokes))
        
class FarmAnimal(Animal):
    def run(self):
        print('run across field')
        
class Cow(FarmAnimal):
    def moo(self):
        print('moooooo')

class Horse(FarmAnimal):
    def whinny(self):
        print('neigh')
        
#skye = Dog('Skye', 2, 0)
#skye.bark()
#skye.eat()
#skye.do_trick()

spider = Cat('Spider', 10)
#spider.meow()
#spider.eat()
#spider_jump_on_human()

#Task Two: Second Example

class Robot():
    def __init__(self, name='robot', speciality='none', age=0):
        self.name = name
        self.speciality = speciality
        self.age = age

    def move(self):
        print('...move move move...')
        
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')

class CookRobot(Robot):
    def cook(self):
        print('I make rice')
        
class DessertCook(CookRobot):
    def bake(self):
        print('I baked cookies')
        
#Task Association: Composition
        
class SuperRobot():
    def __init__(self, name, age):
        self.name = name
        #This class contains 3 objects
        self.o1 = Robot()
        self.o2 = Dog(name)
        self.o3 = CleanRobot()
    def playGame(self):
        print('alphago game')
    def move(self):
        return self.o1.move() #using robot class method
    def bark(self):
        return self.o2.bark() #using dog class method
    def do_trick(self):
        return self.o2.do_trick() #using dog class method
    def clean(self):
        return self.o3.clean() #using cleanrobot method
    
name = sys.argv[1]
age = sys.argv[2]
print(name)
print(age)

machineDog = SuperRobot(name, age)
machineDog.move()
machineDog.bark()