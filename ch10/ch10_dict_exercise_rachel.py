# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:16:48 2018

@author: winkl
"""

#############################################
"""Creating a Dictionary with User Input"""
#############################################

def addKey_phoneBookDict():
    name_key = input("What name would you like to add to the phone book? ")
    return name_key
        
def addItem_phoneBook_dict():
    phoneNo = input("What are the last three digits of their phone number? ")
    luckyNo = input("What is their lucky number? ")
    city = input("Which city are they from? ")
    values = (phoneNo, luckyNo, city)
    return values
    
def continue_phoneBook_dict():
    addItem = input("Would you like to add a person to the phone book? y/n ")[0]
    if addItem == "y":
        generate_phoneBook_dict(phoneBook_dict)
    else:
        print("Ok, your phone book is finished. Here is your finished phone book:")
        
def generate_phoneBook_dict(phoneBook_dict):
    name_key = addKey_phoneBookDict()
    values = addItem_phoneBook_dict()
    phoneBook_dict[name_key] = values
    continue_phoneBook_dict()
    return phoneBook_dict

####Test#####
phoneBook_dict = {}
phoneBook_dict = generate_phoneBook_dict(phoneBook_dict)
print(phoneBook_dict)

##########################################
"""Challenge A: Sorting the Dicitonary"""
##########################################

#Sort by Name
def sortByName():
    orderedName = sorted(phoneBook_dict.items(), key=lambda kv:kv[0])
    print()
    print("The phone book ordered by name:")
    print(orderedName)
    print()
    return orderedName

#Sort by City
def sortByCity():
    orderedCity = sorted(phoneBook_dict.items(), key=lambda kv:kv[1][2])
    print("The phone book ordered by city:")
    print(orderedCity)
    print()
    return orderedCity

#Sort by lucky Number
def sortByLuckyNo():
    orderedluckyNo = sorted(phoneBook_dict.items(), key=lambda kv:kv[1][1])
    print("The phone book ordered by lucky number:")
    print(orderedluckyNo)
    print()
    return orderedluckyNo

def sortThreeWays():
    sortByName()
    sortByCity()
    sortByLuckyNo()
    
######TEST################
sortThreeWays()

#########################################################
"""Challenge B: Add two more items to the values list"""
#########################################################
#
#def makingListKeys():
#    names = list(phoneBook_dict.keys())
#    return names  
#
#def makingListValues():
#    values = list(phonebook_dict.values())
#    return values
#    
#def defineNewValue():
#    age = input("What is {}'s age? ".format(name_key)
#    return age
#    
#def addNewValues_phoneBook_dict():
#    makingListKeys()
#    makingListValues()
#    defineNewValues()
