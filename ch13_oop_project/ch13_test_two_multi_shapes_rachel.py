# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 18:05:56 2018

@author: winkl
"""

from moving_shapes_functions import *

frame = Frame()

numshapes = 3
shapes = []

for i in range(numshapes):
    shapes.append(Square(frame, 100))

for i in range(100):
    for shape in shapes:
        shape.moveTick()