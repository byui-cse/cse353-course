"""
Course: CSE 353
Lesson Week: 11
File: graphics.py
Author: Brother Comeau
Purpose: Drawing class for displaying on the screen
"""

import cv2
import numpy as np

from point import *
from common import *

# -----------------------------------------------------------------------------
class GraphWin:

    def __init__(self, title="Graphics Window", width=400, height=400):

        self.title = title
        self.image = np.zeros((width, height, 3), dtype=np.uint8)

        self.height = int(height)
        self.width = int(width)


    def display(self):
        cv2.imshow(self.title, self.image)


    def setBackground(self, color='FFFFFF'):
        """Set background color of the window"""
        self.image[:] = colorname_to_rgb(color)


    def close(self):
        """Close the window"""
        pass


    def isPixelOn(self, x, y):
        pass


    def clearWindow(self):
        self.setBackground(White)


    def plotPixel(self, x, y, color="000000"):
        """Set pixel raw (independent of window coordinates) pixel (x,y) to color"""
        intX = int(x)
        intY = int(y)
        # print('plot:', intX, intY)

        if (intX >= self.width): return False
        if (intY >= self.height): return False
        if (intX < 0): return False
        if (intY < 0): return False

        self.image[intY, intX] = colorname_to_rgb(color)


    def getHeight(self):
        """Return the height of the window"""
        return self.height


    def getWidth(self):
        """Return the width of the window"""
        return self.width
    
