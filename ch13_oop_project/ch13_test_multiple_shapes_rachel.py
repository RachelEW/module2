# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 21:40:42 2019

@author: winkl
"""

from moving_shapes_functions import *

frame = Frame()

numshapes = 3
shapes = []
size = 60

for i in range(numshapes):
    shapes.append(Square(frame, size))
    shapes.append(Diamond(frame, size))
    shapes.append(Circle(frame, size))

for i in range(300):
    for shape in shapes:
        shape.moveTick()
frame.close()