# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:31:07 2018

@author: winkl
"""

#######################
"""For Loops"""
#######################

#---------------------------------#
"""Task One: writing a for loop"""
#---------------------------------#

my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]
for item in my_shopping_cart:
    print(item)
    
#--------------------------------------------------------#
"""Task Two: Another For Loop and Updating List Values"""
#--------------------------------------------------------#
    
values = [85, 23, 451]
for val in values:
    print('----->'+str(val))
 
for val in values:
    print('---->'+str(val+50))
    
#---Converting a string into a list using split (indicates where to split the sentence)---#
for char in 'Hello, my name is Rachel'.split(' '):
    print(char)

#-------------------------------------------------#
"""Task Three: Creating a For Loop and Printing"""
#-------------------------------------------------#

values = ['this', 55, 'that']
for thing in values:
    print('***', thing)
    
#------------------------------------------------#
"""Task Four: Loop through a string data type"""
#------------------------------------------------#

for char in "Yes":
    print(char)
    
#-----------------------------------#
"""Task Five: Loop thoruh a Tuple"""
#-----------------------------------#

shopping_list2 = ("soap", "shampoo", "conditioner", "toothpaste", "toothbrush")
for bathroom_item in shopping_list2:
    print('--', bathroom_item)
    
#-------------------------------------#
"""Task Six: Loop through a dictionary
COME BACK TO THIS!!!"""
#-------------------------------------#

salary = {'al': 20000, 'bo': 50000, 'ced': 1500}
person = list(salary.keys())
print(person)
print()

###---Using Dicitonary from ch10---###

#-----------------------------------------------------#
"""Task Seven: Example - Loop throught a dictionary"""
#-----------------------------------------------------#

#type of metal:density, stock price
metals = {'iron': (7, 23), 'gold': (19.3, 30), 'zinc': (7.13, 18), 'lead': (11.4, 19)}

#converting metal key values into a list
metals_keys = list(metals.keys())
print(metals_keys)

#sort using sort() in reverse value order
metals_keys.sort(reverse = True, key=lambda k:metals[k])
print(metals_keys)

#sorted key:value pair
sorted_metalDensity = sorted(metals.items(), key=lambda kv:kv[1])
print(sorted_metalDensity)

###-----------------------###
"""Task Seven: Option One"""
###-----------------------###

#printing printing based on the first value(metal) using for loop
for abc in sorted_metalDensity:
    print(abc)
    print()
    
#printing the sorted:key value pairs using a for loop
for abc in sorted_metalDensity:
    print(abc[0], 'has a density of', abc[1][0]) #select items within the list and tuple

###-----------------------###
"""Task Seven: Option Two"""
###-----------------------###

print('\nHere\'s a list of the metals and their stock price')
for k, v in sorted_metalDensity:
    print(k, '=', v[1])
#for item, metalValue in metal_density:
#    print(metal, metalValue[1])

"""COME BACK TO THIS!!!!!!!!!"""
#for metal in metals:
#    if metals[metal] [0]>8:
#        print('{0:>8} = {1:5.1f}'.format(metal, sorted_metalDensity[1][0]))
#.1f give float to the precision of 1 decimal place
#In {1:5} the second number sets the alignment the item it is formatting. > means right-align text in the field

#for metal in sorted_metalDensity:
#    print('{0:>8} = {1:5.1f}'.format(sorted_metalDensity[0], sorted_metalDensity[1]))

#--------------------------------------------------------------#
"""Task Eight: using IF ELSE to search for a particular value"""
#--------------------------------------------------------------#

print('\nMetals with a density over 8:')
for abc in sorted_metalDensity:
    if abc[1][0] > 8:
        print(abc[0], 'has a density of', abc[1][0])
    
#----------------------------------------------------------------------#
"""Task Nine: Computing the sum of values in a list using a for loop"""
#----------------------------------------------------------------------#
    
valuesList = [3, 12, 9]

total = 0
print('\nUpdating the value of the total by adding items one by one:')
for value in valuesList:
    print('before adding', value, 'the total is', total)
    total += value
    print('after adding', value, 'the total is', total)    
print('OVERALL TOTAL: ' + str(total))


#---------------------------------------------#
"""Task Ten: Using a Loop with Index Values"""
#---------------------------------------------#

values = [3, 12, 9]
for index in range(len(values)):
    values[index] = values[index] * 2
print("\n",values)

for index in range(len(values)):
    print(values[index] )


#--------------------------#
"""Task Eleven: step size"""
#--------------------------#

for i in list(range(3, 10, 2)):
    print(i)
    
#---------------------------------------------------#
"""Task 12: Breaking a list above a certain value"""
#---------------------------------------------------#
    
scan_list = [1, 5, 30, 200, 101, 100, 22]

for i in scan_list:
    if i > 100:
        print('stop!')
        break
    else:
        print('keep going')
        
for index in range(len(scan_list)):
    if scan_list[index] > 100:
        print('break:', scan_list[index], 'with index',index)
        break

#-------------------------------------#
"""Extra exercise: using a counter"""
#-------------------------------------#
        
colours = ['red', 'green', 'red', 'green', 'blue', 'green', 'green']
d = {} # build an empty dictionary
for item in colours:
    if item not in d:
        d[item] = 0
        print(d, 'first mention')
    else:
        d[item] += 1
        print(d)
print('Final Dictionary:',d)

#--------------------------------#
"""Task Thirteen: Nested loops"""
#--------------------------------#

outer_vals = [1, 2, 3]
inner_vals = ['a', 'b', 'c']
for oval in outer_vals:
    for ival in inner_vals:
        print(oval, ival)

d2 = {}        
for oval in outer_vals:
#    print(oval)
    for ival in inner_vals:
#        print(ival)
        d2[oval] = ival
        print(d2)
print(d2)

#----------------------------------------#
"""Task Fourteen: multiplication table"""
#----------------------------------------#

#multiplication table 7 x 10
for i in list(range(1,7)):
    for j in range(1, 11):
        print('{0:>3}'.format(i*j), end=' ') #end=' ' creates a space at the end
    print('\n')
    
#multiplication table 10 x 10
for i in list(range(1,11)):
    for j in range(1, 11):
        print('{0:>3}'.format(i*j), end=' ') #end=' ' creates a space at the end
    print('\n')