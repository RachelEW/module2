# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 15:53:23 2018

@author: winkl
"""

#-----------------------------------------------------------
"""sleep_in
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation.
Return True if we sleep in."""
#-----------------------------------------------------------

def sleep_in(weekday, vacation):
  if vacation == True:
    return True
  elif weekday == False:
    return True
  else:
    return False

#---------------------------
"""monkey_trouble"""
#---------------------------

def monkey_trouble(a_smile, b_smile):
  if a_smile == True and b_smile == True:
    return True
  elif a_smile == False and b_smile == False:
    return True
  else:
    return False

#-------------------------
"""sum_double"""
#-------------------------

def sum_double(a, b):
  if a == b:
    return (a + b) * 2
  else:
    return a + b

#-------------------------
"""diff21"""
#-------------------------

def diff21(n):
  if n > 21:
    return (n-21)*2
  else:
    return 21-n

#--------------------
"""parrot_trouble"""
#--------------------

def parrot_trouble(talking, hour):
  if talking == True and hour > 20:
    return True
  elif talking == True and hour < 7:
    return True
  else:
    return False

#--------------------
"""makes10"""
#--------------------

def makes10(a, b):
  if a== 10 or b == 10:
    return True
  elif a + b == 10:
    return True
  else:
    return False

#-------------------#
"""near_hundred
Given an int n, return True if it is within 10 of 100 or 200.
Note: abs(num) computes the absolute value of a number."""
#-------------------#

def near_hundred(n):
  if n >= (100-10) and n <= (100+10):
    return True
  elif n >= (200-10) and n <= (200+10):
    return True
  else:
    return False

#--------------------#
"""pos-neg
Given 2 int values, return True if one is negative and one is positive.
Except if the parameter "negative" is True, then return True only if both are negative."""
#--------------------#

def pos_neg(a, b, negative):
  if a > 0 and b < 0 and negative == False:
    return True
  elif a < 0 and b > 0 and negative == False:
    return True
  elif a < 0 and b < 0 and negative == True:
    return True
  else:
    return False

#-----------------#
"""not_string
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged."""
#-----------------#

def not_string(str):
  if str[0:3] == "not":
    return str
  else:
    return "not " + str

#-----------------#
"""missing_char
Given a non-empty string and an int n, return a new string where the char at index n has been removed.
The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive)."""
#-----------------#

