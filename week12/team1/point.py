"""
Course: CSE 353
Lesson Week: 11
File: point.py
Author: Brother Comeau
Purpose: Proint class
"""
import numpy as np
import math
from matrix import *

class Point:
    def __init__(self, x=0, y=0):
        self.values = [float(x), float(y), 1.0]

    def __repr__(self):
        return f"({self.values[0]:10.2f}, {self.values[1]:10.2f}, {self.values[2]:10.2f})"

    def getX(self):
        return self.values[0]

    def getY(self):
        return self.values[1]

    def setX(self, value):
        self.values[0] = value

    def setY(self, value):
        self.values[1] = value

    # Returns a new point from the expression -> Point * Matrix
    def __mul__(self, m):
        tmp = Point()
        tmp.setX(m.mat[0][0] * self.values[0] + m.mat[0][1] * self.values[1] + m.mat[0][2])
        tmp.setY(m.mat[1][0] * self.values[0] + m.mat[1][1] * self.values[1] + m.mat[1][2])
        return tmp

