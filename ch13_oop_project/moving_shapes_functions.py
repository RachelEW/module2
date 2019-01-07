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

class MovingShape():
    def __init__(self, frame, shape, diameter, x=0, y=0, dx=0, dy=0, minx=0, minxy=0, maxx=0, maxy=0):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        self.frame = frame
        self.x = self.defineStartX()
        self.y = self.defineStartY()
        self.dx = self.moveSpeedX()
        self.dy = self.moveSpeedY()
        
    def goto(self, x, y):
        self.figure.goto(x, y)
        
    def moveTick(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy 
        self.goto(self.x, self.y)
        self.checkEdgeXAxis()
        self.checkEdgeYAxis()

###---Setting Shape Velocity---###
    def moveSpeedX(self):
        self.dx = 5 + 10 * r()
        if r() > 0.5:
            self.dx = 0 - self.dx
        return self.dx
        
    def moveSpeedY(self):
        self.dy = 5 + 10 * r()
        if r() > 0.5:
            self.dy = 0 - self.dy
        return self.dy 
    
###---Reverse Velocity at Edges of Frame---###
    def checkEdgeXAxis(self):
        if self.x < self.minx:
            self.dx = self.dx * -1
        elif self.x > self.maxx:
            self.dx = self.dx * -1
        return self.dx
    
    def checkEdgeYAxis(self):
        if self.y < self.miny:
            self.dy = self.dy * -1
        elif self.y > self.maxy:
            self.dy = self.dy * -1
        return self.dy
    
###---Set minimum and maximum (x,y) coordinates---###
    def defineMinX(self):
        self.minx = self.diameter / 2
        return self.minx
    
    def defineMaxX(self):
        d2 = self.diameter / 2
        self.maxx = self.frame.width - d2
        return self.maxx
    
    def defineMinY(self):
        self.miny = self.diameter / 2
        return self.minx
    
    def defineMaxY(self):
        d2 = self.diameter / 2
        self.maxy = self.frame.height - d2
        return self.maxy
    
###---Choose Random Initial Coordinates---###
    def defineStartX(self):
        self.defineMinX()
        self.defineMaxX()
        self.x = self.minx + r() * (self.maxx - self.minx)
        return self.x
    
    def defineStartY(self):
        self.defineMinY()
        self.defineMaxY()
        self.y = self.miny + r() * (self.maxy - self.miny)
        return self.y
        
class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'square', diameter)
        
class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'diamond', diameter)

###---Set minimum and maximum (x,y) coordinates for Diamond---###
    def defineMinX(self):
        a1 = self.diameter**2 + self.diameter**2
        a2 = a1**0.5
        self.minx = a2 / 2
        return self.minx
    
    def defineMaxX(self):
        a1 = self.diameter**2 + self.diameter**2
        a2 = a1**0.5
        a3 = a2 / 2
        self.maxx = self.frame.width - a3
        return self.maxx
    
    def defineMinY(self):
        a1 = self.diameter**2 + self.diameter**2
        a2 = a1**0.5
        self.miny = a2 / 2
        return self.miny
    
    def defineMaxY(self):
        a1 = self.diameter**2 + self.diameter**2
        a2 = a1**0.5
        a3 = a2 / 2
        self.maxy = self.frame.height - a3
        return self.maxy
        
class Circle(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'circle', diameter)
        

    