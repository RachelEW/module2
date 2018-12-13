# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:25:44 2018

@author: 612383461
"""
#######################
"""LPTHW ch04"""
#######################

#ex11

#print("How old are you?")
#age = input()
#print("How tall are you?")
#height = input()
#print("How much do you weight?")
#weight = input()
#
#print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

#ex12

#age = input("How old are you? ")
#height = input("How tall are you? ")
#weight = input("How much do you weigh? ")
#
#print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))
#
###ex29
#
#people = 20
#cats = 30
#dogs = 15
#
#if people < cats:
#    print("Too many cats! The world is doomed!")
#    
#if people > cats:
#    print("Not many cats! The world is saved!")
#    
#if people < dogs:
#    print("The world is drooled on!")
#        
#if people > dogs:
#    print("The world is dry")
#    
#dogs += 5
##means dogs = dogs + 5
#
#if people >= dogs:
#    print("People are greater than or equal to dogs.")
#
#if people <= dogs:
#    print("People are less than or equal to dogs.")
#    
#if people == dogs:
#    print("People are dogs.")
    
#ex30
#
#people = 30
#cars = 40
#buses = 15
#
#if cars > people:
#    print("We should take the cars.")
#elif cars < people:
#    print("We should not take the cars.")
#else:
#    print("We can't decide.")
#
#if buses > cars:
#    print("That's too many nuses.")
#elif buses < cars:
#    print("Maybe we could take the buses.")
#else:
#    print("We still can't decide.")
#
#if people > buses:
#    print("Alright, let's just take the buses.")
#else:
#    print("Fine, let's stay home then.")
    

#ex31
  
print ("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
    print("There's a agiant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    
    bear = input("> ")
    
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")
else:
    print("You stumble around and fall on a knife and die. Good job!")
