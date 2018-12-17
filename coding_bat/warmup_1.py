# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 15:53:23 2018

@author: winkl
"""

"""The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation.
Return True if we sleep in."""

def sleep_in(weekday, vacation):
  if vacation == True:
    return True
  elif weekday == False:
    return True
  else:
    return False

