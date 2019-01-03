# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 16:24:42 2018

@author: winkl
"""

#########################
"""OOP Shapes Project"""
#########################

from Shapes import * 

x = 0
y = 0

frame = Frame()
s1 = Shape('square',100)
s1.goto(200,100)
#frame.close()

for i in range(100):
    s1.goto(x,y)
    x = x + 5
    y = y + 5

