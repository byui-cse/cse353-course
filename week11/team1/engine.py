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

        # TODO - add variables as needed for projects

        self.width = width
        self.height = height

        self.offset_x = 0
        self.offset_y = 0

        self.scale_mat = Matrix3('I')
        self.rotation_mat = Matrix3('I')
        self.trans_mat = Matrix3('I')

        self.win.setBackground(White)


    def world_offset(self, x, y):
        self.offset_x = x
        self.offset_y = y


    def createTRS(self):
        return (self.trans_mat * self.rotation_mat * self.scale_mat)


    def dot(self, x, y, color='000000'):
        pt = Point(x, y) * self.createTRS()
        self.win.plotPixel(pt.getX() + self.offset_x, pt.getY() + self.offset_y, color)


    def rotation(self, rot):
        self.rotation_mat.rotation(rot)
        # print(self.mat)


    def scale(self, x, y):
        self.scale_mat.scale(x, y)
        # print(self.mat)


    def translate(self, x, y):
        self.trans_mat.translation(x, y)


    def display(self):
        self.win.display()


    def wait(self, amount):
        self.display()
        cv2.waitKey(amount)


    def close(self):
        pass

    # --------------------------------------------------------------------------
    # print() formatting
    def __str__(self):
        # TODO - This function is called by the Python print() function, add what you want
        return 'display TODO'
