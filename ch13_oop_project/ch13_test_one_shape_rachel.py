# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 17:02:14 2018

@author: winkl
"""

from moving_shapes_functions import *

frame = Frame()
shape1 = Square(frame, 100)

for i in range(100):
    shape1.moveTick()
    
#frame.close()