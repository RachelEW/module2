# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:38:39 2019

@author: winkl
"""

###################
"""List-2"""
###################

#----------------------------------------------------------------------#
"""Return the number of even ints in the given array.
Note: the % "mod" operator computes the remainder, e.g. 5 2 is 1.

count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0"""
#----------------------------------------------------------------------#

def count_evens(nums):
  count = 0
  for num in nums:
    if num % 2 == 0:
      count += 1
  return count

print(count_evens([2, 1, 2, 3, 4]))


#-----------------------------------------------#
"""has22

Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False"""
#-----------------------------------------------#

def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == 2:
          if nums[i+1] == 2:
            return True
  return False

print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))