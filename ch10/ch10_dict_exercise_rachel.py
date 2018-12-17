# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:16:48 2018

@author: winkl
"""

#############################################
"""Creating a Dictionary with User Input"""
#############################################

def addKey_phoneBook_dict():
    name_key = input("What name would you like to add to the phone book? ")
    return name_key
        
def addItem_phoneBook_dict():
    QueensAge = 92
    phoneNo = input("What are the last three digits of their phone number? ")
    luckyNo = input("What is their lucky number? ")
    city = input("Which city are they from? ")
    age = input("What is their age? ")
    diffQueenAge = QueensAge - int(age)
    values = [phoneNo, luckyNo, city, age, diffQueenAge]
    return values
    
def continue_phoneBook_dict():
    addItem = input("Would you like to add a person to the phone book? y/n ")[0]
    if addItem == "y":
        generate_phoneBook_dict(phoneBook_dict)
    else:
        print("Ok, your phone book is finished. Here is your finished phone book:")
        
def generate_phoneBook_dict(phoneBook_dict):
    name_key = addKey_phoneBook_dict()
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
"""Challenge B"""
#########################################################

####Difference in Age from Queen's Age####

#def compare_QueensAge(phoneBook_dict):
#    QueensAge = 92
#    
#    valuesList = list(phoneBook_dict.values())
#    print(valuesList)
#    
#    ages = agesList[0][3]
#    print(ages)
#    ageList = sorted(phoneBook_dict.items(), key=lambda kv:kv[1][3])
#    print(ageList)
#    print(phoneBook_dict.get(name_key[3]))
#    

####Writing the final Dictionary to a file####

f = open('phonebook.txt','w')
f.write(str(phoneBook_dict))
f.close()
##
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
