# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:55:33 2018

@author: winkl
"""

{'bo':5000, 'al':20000, 7:('Joke', 'Chen', 'Bond')}

######################
"""Dictionarys"""
######################

#creating an empty dictionary

salary = {}
salary['al'] = 20000

print(salary)

favourite_number = {}
favourite_number['Sally'] = 7
favourite_number['Jess'] = 12
print(favourite_number)

#Phonebook Example

phone_book = {'Rachel':819, 'Aminat': '051', 'Tilly': 369}
print(phone_book)

phone_book['Sally'] = 234
print(phone_book)

phone_book['Rachel'] = 9819
print(phone_book)

#to delete an item

del phone_book['Sally']
print(phone_book)

print(phone_book.keys()) #get list of keys (non-standard list)
print(phone_book.values())
#these are not lists, the data types are dict_keys and dict_values

phone_book_keys = list(phone_book.keys())
#make it a list to be able to use methods on the list adn to retrieve items

print(phone_book_keys[0])

############################
"""Testing for errors"""
############################

k = 'Eric'
if k in phone_book:
    print(k, ':', phone_book[k])
else:
    print(k, 'not found!')#more informative error message
    
#######################
"""Sorting"""
#######################

counts = {'a': 3, 'c': 1, 'b': 5}
labels = list(counts.keys())
print(labels)

labels.sort(key=lambda k:counts[k]) #k is a generic variable which represents key
print(labels)

#multiple values

person = {'Jess':('AJanuary', 23, 'cat'), 'ASally':('December', 12, 'dog'), 'Molly':('February', 31, 'tiger')}
lucky_number = list(person.keys())
print(lucky_number)

lucky_number.sort(key=lambda k:person[k][1]) #sorting by the second value
print(lucky_number)

#return both key and values in sort

x = sorted(person.items(), key=lambda kv:kv[1][2]) #first number chooses key or value, then second number chooses value in tuple
print(x)

###########################
"""Task: Sorting Metals"""
###########################'

#type of metal:(density, share price, no. of experiments)
metals = {'iron':(7.8, 7.87, 0.432), 'gold': (19.3, 23.63, 0.031), 'zinc':(7.13, 6.90, 0.284), 'lead':(11.4, 13.82, 0.317)}

#sort dict's second value in descending order

sort_by_share_price = sorted(metals.items(), key=lambda kv:kv[1][1])
print(sort_by_share_price)

#to sort in reverse order

reverse_name = sorted(metals.items(), key=lambda kv:kv[0], reverse=True)
print(reverse_name)

#sort using sort()

metals_keys = list(metals.keys())
metals_keys.sort(key=lambda k:metals[k])
print(metals_keys)

top_share_price = sorted(metals.items(), key=lambda kv:kv[1][1])[0] #the final[0] splits the list and means that only the first result will be listed
print(top_share_price)