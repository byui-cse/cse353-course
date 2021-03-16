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

        self.scale_mat = Matrix3('Identy')
        self.rotation_mat = Matrix3('Identy')
        self.trans_mat = Matrix3('Identy')

        self.win.setBackground(White)


    def set_offset(self, x, y):
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

    """
        def _plotLineLow(self, x0, y0, x1, y1):
            dx = x1 - x0
            dy = y1 - y0
            yi = 1
            if dy < 0:
                yi = -1
                dy = -dy

            D = 2*dy - dx
            y = y0

            for x in frange(x0, x1):
                self._displayPixel(x, y)
                if D > 0:
                    y = y + yi
                    D = D - 2*dx
                D = D + 2*dy


        def _plotLineHigh(self, x0, y0, x1, y1):
            dx = x1 - x0
            dy = y1 - y0
            xi = 1
            if dx < 0:
                xi = -1
                dx = -dx
            D = 2*dx - dy
            x = x0

            for y in frange(y0, y1):
                self._displayPixel(x,y)
                if D > 0:
                    x = x + xi
                    D = D - 2*dy
                D = D + 2*dx

        def _plotLine(self, x0,y0, x1,y1):
            if math.fabs(y1 - y0) < math.fabs(x1 - x0):
                if x0 > x1:
                    self._plotLineLow(x1, y1, x0, y0)
                else:
                    self._plotLineLow(x0, y0, x1, y1)
            else:
                if y0 > y1:
                    self._plotLineHigh(x1, y1, x0, y0)
                else:
                    self._plotLineHigh(x0, y0, x1, y1)



        def _addToFloodStack(self, stack, r, c):
            pt = Point(r, c)
            pt2 = pt * self.createTRS()

            if (pt2.getX() >= self.width): return
            if (pt2.getY() >= self.height): return
            if (pt2.getX() <= 0): return
            if (pt2.getY() <= 0): return

            if (self.win.isPixelOn(pt2.getX(), pt2.getY()) == False):
                stack.append((r, c))

        # --------------------------------------------------------------------------
        # This function will fill an area using 4 directional fill alogrithm
        # The self.win object has the methods:
        #     isPixelOn()
        #     clearWindow()
        def floodfill(self, x, y, color='black'):
            stack = [(x, y)]
            count = 0
            self._addToFloodStack(stack, x, y)
            while (len(stack) > 0):
                # pop a point
                r, c = stack.pop()
                # print(r, c, self.pos)

                if (self.win.isPixelOn(r, c) == False):
                    self._displayPixel(r, c, color)
                    count += 1
                    if (count % 3000 == 0):
                        self.flush()

                    # push on stack
                    self._addToFloodStack(stack, r + 1, c)
                    self._addToFloodStack(stack, r - 1, c)
                    self._addToFloodStack(stack, r, c + 1)
                    self._addToFloodStack(stack, r, c - 1)
    """
