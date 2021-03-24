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
  
        self.scale_mat = Matrix3('I')
        self.rotation_mat = Matrix3('I')
        self.trans_mat = Matrix3('I')

        self.trs = self._createTRS()
        self.win.setBackground(White)


    def clear(self):
        self.win.clearWindow()


    def dot(self, x, y, color='000000'):
        pt = Point(x, y) * self._createTRS()
        self.win.plotPixel(pt.getX(), pt.getY(), color)


    def draw_dot(self, x, y, trs, color='000000'):
        pt = Point(x, y) * trs * self.trs
        self.win.plotPixel(pt.getX(), pt.getY(), color)
        pass

    def draw_line(self, pt1, pt2, trs, color='000000'):
        if trs == None:
            p1 = pt1 * self.trs
            p2 = pt2 * self.trs
        else:
            p1 = pt1 * trs * self.trs
            p2 = pt2 * trs * self.trs
            
        points = self._plotLine(p1.getX(), p1.getY(), p2.getX(), p2.getY())
        for pt in points:
            self.win.plotPixel(pt.getX(), pt.getY(), color)


    def rotation(self, rot):
        self.rotation_mat.rotation(rot)
        self.trs = self._createTRS()

    def scale(self, x, y):
        self.scale_mat.scale(x, y)
        self.trs = self._createTRS()

    def translate(self, x, y):
        self.trans_mat.translation(x, y)
        self.trs = self._createTRS()


    def display(self):
        self.win.display()


    def wait(self, amount):
        self.display()
        cv2.waitKey(amount)


    def close(self):
        pass

    def _createTRS(self):
        return (self.trans_mat * self.rotation_mat * self.scale_mat)

    # --------------------------------------------------------------------------
    # print() formatting
    def __str__(self):
        # TODO - This function is called by the Python print() function, add what you want
        return 'display TODO'


    def _plotLine(self, x0, y0, x1, y1):
        if math.fabs(y1 - y0) < math.fabs(x1 - x0):
            if x0 > x1:
                return self._plotLineLow(x1, y1, x0, y0)
            else:
                return self._plotLineLow(x0, y0, x1, y1)
        else:
            if y0 > y1:
                return self._plotLineHigh(x1, y1, x0, y0)
            else:
                return self._plotLineHigh(x0, y0, x1, y1)

    def _plotLineLow(self, x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0
        yi = 1
        if dy < 0:
            yi = -1
            dy = -dy

        D = 2*dy - dx
        y = y0

        points = []
        for x in frange(x0, x1):
            points.append(Point(x, y))
            if D > 0:
                y = y + yi
                D = D - 2*dx
            D = D + 2*dy
        return points


    def _plotLineHigh(self, x0,y0, x1,y1):
        dx = x1 - x0
        dy = y1 - y0
        xi = 1
        if dx < 0:
            xi = -1
            dx = -dx
        D = 2*dx - dy
        x = x0

        points = []
        for y in frange(y0, y1):
            points.append(Point(x, y))
            if D > 0:
                x = x + xi
                D = D - 2*dy
            D = D + 2*dx
        return points
