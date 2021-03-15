"""
Course: CSE 353
Lesson Week: 11
File: engine.py
Author: Brother Comeau
Purpose: Drawing engine
"""

from graphics import *
from matrix import *
from point import *
from common import *
import math


# --------------------------------------------------------------------------
# Vec2D class
# This class is used by some of the method in Engine
class Vec2D():

    def __init__(self, x, y = None):
        if (y == None):
            self.dx = x.getDx()
            self.dy = x.getDy()
        else:
            self.dx = x
            self.dy = y

    def getDx(self):
        return self.dx

    def getDy(self):
        return self.dy

    def setX(self, value):
        self.dx = value

    def setY(self, value):
        self.dy = value

    def getDistance(self):
        return math.sqrt(self.dx * self.dx + self.dy * self.dy)

    def getAngle(self):
        return rad2deg(math.atan2(-self.dy, self.dx))

    def _setXY(self, radians, dist):
        self.dx = math.cos(radians) * dist
        self.dy = -math.sin(radians) * dist

    def setVector(self, angle, distance):
        self._setXY(deg2rad(angle), distance)

    def setDistance(self, distance):
        self._setXY(deg2rad(self.getAngle()), distance)

    def setAngle(self, angle):
        self._setXY(deg2rad(angle), self.getDistance())


# --------------------------------------------------------------------------
class Engine():

    def __init__(self, title="Graphics Window", width=400, height=400):

        # Create the drawing context
        self.win = GraphWin(title, width, height)

        self.width = width
        self.height = height

    def dot(self, x, y, color='black'):
        """ Draw a dot """
        self.win.plotPixel(x, y, color)        

    def createTRS(self):
        return (self.trans_mat * self.rotation_mat * self.scale_mat)


    def rotation(self, rot):
        pass


    def scale(self, x, y):
        pass


    def translate(self, x, y):
        pass


    def flush(self):
        """
        This function forces any drawing that your program has done to be drawn in the window
        Calling this function too many times, will slow down your program
        """
        self.win.flush()




    # --------------------------------------------------------------------------
    # The following functions are here to help interacting with the user in the main screen.

    def getMouse(self):
        """ Get the position where the mouse was clicked in the window """
        return self.win.getMouse()

    def checkMouse(self):
        """ Return last mouse click or None if mouse has not been clicked since last call """
        return self.win.checkMouse()

    def getKey(self):
        """ Wait for user to press a key and return it as a string """
        return self.win.getKey()

    def checkKey(self):
        """ Return last key pressed or None if no key pressed since last call """
        return self.win.checkKey()

    def getHeight(self):
        """ Return the height of the window """
        return self.height

    def getWidth(self):
        """ Return the width of the window """
        return self.width

    def setMouseHandler(self, func):
        """ Define your own mouse handler function """
        self.win.setMouseHandler(func)

    def __str__(self):
        """ This function is called by the Python print() function, add what you want """
        return 'display TODO'

    # Call this to finish any program that you use the engine
    def close(self):
        self.win.close()
