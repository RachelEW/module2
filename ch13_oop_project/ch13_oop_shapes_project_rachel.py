# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 16:52:33 2018

@author: winkl
"""

####################
"""Shapes Project"""
####################

from Shapes import *
from pylab import random as r

class MovingShape:
    def __init__(self, frame, shape, diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(Shape, diameter)
    def goto(self, x, y):
        self.figure.goto(x, y)
    def moveTick(Self):
        pass
    
class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(Self, frame, 'square', diameter)
        
class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'diamond', diameter)
    
class Circle(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'cirle', diameter)
        

    