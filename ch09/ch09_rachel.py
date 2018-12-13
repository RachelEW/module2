# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:28:27 2018

@author: winkl
"""

#############
"""Lists"""
#############

#lists are mutable (they can be changed)

my_favourite_fruits = ['apple', 'orange', 'banana']

x = ['this', 55, 'that', my_favourite_fruits] #list can contain mix type of data

#print(x[0])
#print(x[1])
#print(x[2])
#print(x[-1])
#print(x[-2])
#print(x[-1][-3]) #first position goes into the item my_favourite_fruits, the second number relates to an item within that
#print(x[-2][-3]) #first no. picks the item, second no. selects the letter within that string

x.remove(my_favourite_fruits) #remove only applies to lists
print(x)

x[1] = 'and' #update list item value by using indew of the item in the current list
print(x)

x.append('again') #append only applies to list, adds item to the end of the list
print(x)


x = ['the', 'cat', 'sat']
y = ['on', 'the', 'mat']
z = x + y
print(z)
print(z*3)
a = set(x + y) #Changes a list into a dictionary and removes repeated items.
print(a)

x = ['this', 'and', 'that', 'once', 'again']
print(x[-2:3])

####################
"""Sorting Lists"""
####################

x = [7, 11, 2, 9, 2]

y = sorted(x) #creates a new list, assign to a new variable
print(y)

x.sort() #sorts the exiting list
print(x)

x = ['ab', 'cs', 'yw', 'zs', 'hd']
y = sorted(x)
print(y) #sorts by the first letter fo the string
x.sort()
print(x)

###########################
"""Reverse Sorting Lists"""
###########################

x = [7, 11, 2, 9, 2]
y = sorted(x,reverse=True)
print(y)

x.sort(reverse=True)
print(x)

x = ['ab', 'cs', 'yw', 'zs', 'hd']
y = sorted(x,reverse=True)
print(y)

x.sort(reverse=True)
print(x)

x.sort(reverse=True)
print(x)

##################
"""Tuples"""
##################

a = [0,1,2,3,4,5,6,7,8,9] #list
del a[-1]
a[0] = 50 #adds a list element at the specified place in the list
a.append('z')

b = (0,1,2,3,4,5,6,7,8,9) #Tuple
#del b[-1] #Tuple does't support item deletion #means people can't edit your lists
#b[0] = 50 #Tuple deos not support this
#b.append('z') #cannot use append on a Tuple

#############
"""Lambada"""
#############

#use lambda functions when we require a nameless function for a short period of time.

a = [50, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = ['aa', 'zs', 'cs', 'hd', 'ab']
y = ['ab', 'cs', 'hs', 'yw', 'zs']
z = ['zs', 'yw', 'hd', 'cs', 'ab']
y = sorted(x)

x2 = [('a', 3, z), ('c', 1, y), ('b', 5, x)]

print(x2)
print("\n")

print(sorted(x2, key=lambda s:s[2][1])) #x2 is a variable, in the function is replaces 's', sorts by the second item (looks at the item which is in position [1])
#sorted(x2, ky=lamba variablePlaceHolder:variablePlaceHolder[1])

#Example(Iza)
#this list includes 3 tuples. each contains a string, a number and a variable
x2 = [('Kate', 3, z), ('Joanna', 1, y), ('Betty', 5, x)]

print("------print(x2)------")
print (x2)
print()
print("------print(sorted(x2, key=lambda s:s[1]))------")
print(sorted(x2, key=lambda s:s[1]))
#this is organized by what is at the first position in the tuple - number in this case