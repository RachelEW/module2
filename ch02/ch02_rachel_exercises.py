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

my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print ("Let's talk about %s" % my_name)
print ("He's %d inches tall." % my_height)
print ("He's %d pounds heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)

print ("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print (x)
print (y)

print ("I said: %r." % x)
print ("I also said: '%s'." %y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious)

w = ("This is the left side of...")
e = ("a string with a right side.")

print (w + e)

print ("Mary had a little lamb.")
print ("Its fleece was white as %s." % 'snow')
print ("And everywhere that Mary went.")
print ("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print (end1 + end2 + end3 + end4 + end5 + end6,
end7 + end8 + end9 + end10 + end11 + end12)

formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "So I said goodnight."
        ))

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print ("Here are the days: ", days)
print ("Here are the months: ", months)

print ("""
       There's something going on here.
       With the three double-quotes.
       We'll be able to type as much as we like.
       Even 4 lines if we want, or 5, or 6.
       """)

tabby_cat = "\tI'm tabbed in."
persian_cat ="I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* fishies
\t* Catnip\n\t* Grass
"""
    
print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)