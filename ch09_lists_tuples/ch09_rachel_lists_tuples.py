# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:28:27 2018

@author: winkl
"""

#############
"""Lists"""
#############

#lists are mutable (they can be changed)

#-------------------------------------------------#
"""Task One: Creating and Using index in a List"""
#-------------------------------------------------#

my_favourite_fruits = ['apple', 'orange', 'banana']
x = ['this', 55, 'that', my_favourite_fruits] #lists can contain a mix of data types

#print(x[0])
#print(x[1])
#print(x[2])
#print(x[-1])
#print(x[-2])
#print(x[-1][-3]) #first position goes into the item my_favourite_fruits, the second number relates to an item within that
#print(x[-2][-3]) #first no. picks the item, second no. selects the letter within that string

#----------------------------#
"""Task Two: Modify a List"""
#----------------------------#

#deleting an item in a list
x.remove(my_favourite_fruits) #remove only applies to lists
print(x)

#updating (replacing) a list item value by using the indew of the item in the current list
x[1] = 'and'
print(x)

#adding an item to the end of a list
x.append('again') #append only applies to lists
print(x)

w = ['the', 'cat', 'sat']
y = ['on', 'the', 'mat']
z = w + y
print(z)
print(z*3)

#Using Set
#Changes a list into a dictionary and removes repeated items.
a = set(w + y)
print(a)

#------------------------------#
"""Task Three: Slicing Lists"""
#------------------------------#

x = ['this', 'and', 'that', 'once', 'again']

print(x[1:4]) #includes items in positions 1-3, does not include 4
print(x[-2:3])

print(z)
print(z[3:10])

#---------------------------#
"""Tasks 4: Sorting Lists"""
#---------------------------#

x = [7, 11, 2, 9, 2]

y = sorted(x) #creates a new list, assign to a new variable
print(y)
print(x)

x.sort() #sorts the exiting list
print(x)

x = ['ab', 'cs', 'yw', 'zs', 'hd']
y = sorted(x)
print(y) #sorts by the first letter of the string
x.sort()
print(x)

#-------------------------#
"""Reverse Sorting Lists"""
#-------------------------#

x = [7, 11, 2, 9, 2]
y = sorted(x,reverse=True) #creates a new list
print(y)

x.sort(reverse=True) #sorts the existing list
print(x)

x = ['ab', 'cs', 'yw', 'zs', 'hd']
y = sorted(x,reverse=True)
print(y)

x.sort(reverse=True)
print(x)

##################
"""Tuples"""
##################

#tuples are immutable (they can't be changed)

#-------------------------------#
"""Comparing lists and tuples"""
#-------------------------------#

#List Example
a = [0,1,2,3,4,5,6,7,8,9] #list
del a[-1]
a[0] = 50 #adds a list element at the specified place in the list
a.append('z')

#Tuple Example
b = (0,1,2,3,4,5,6,7,8,9) #Tuple
#del b[-1] #Tuples do not support item deletion #means people can't edit your lists
#b[0] = 50 #Tuples do not support this
#b.append('z') #cannot use append on a Tuple

#################
"""Lambada"""
#################

#----------------------------------------#
"""Task 6: Using lambda to sort a list"""
#----------------------------------------#

#use lambda functions when we require a nameless function for a short period of time.
#used for more complicated sorts

a = [50, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = ['aa', 'zs', 'cs', 'hd', 'ab']
y = ['ab', 'cs', 'hs', 'yw', 'zs']
z = ['zs', 'yw', 'hd', 'cs', 'ab']
y = sorted(x)

x2 = [('a', 3, z), ('c', 1, y), ('b', 5, x)]

print(x2)
print("\n")

print(sorted(x2, key=lambda s:s[2][1])) #x2 is a variable, in the function is replaces 's', sorts by the second item (looks at the item which is in position [1])

#---Syntax---#
#sorted(x2, key=lamba variablePlaceHolder:variablePlaceHolder[1])

#---------------------#
"""Another Example"""
#---------------------#

#this list includes 3 tuples. each contains a string, a number and a variable
x2 = [('Kate', 3, z), ('Joanna', 1, y), ('Betty', 5, x)]

print("------print(x2)------")
print (x2)
print()
print("------print(sorted(x2, key=lambda s:s[1]))------")
print(sorted(x2, key=lambda s:s[1]))
#this is organized by what is at the first position in the tuple - in this case the number