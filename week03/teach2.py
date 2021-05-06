"""
Course: CSE 353
Lesson Week: 03
File: teach2.py
Author: Brother Comeau
Instructions: Look for the TODO in comments
"""

import time
import cv2
from matplotlib.pylab import plt
import numpy as np


def fill_shapes():
    image = cv2.imread('shapes.png')

    """
    TODO

    Use a recursive function to fill in the different shapes in the "shapes.png" image
    Don't use any opencv fill functions - just numpy accessing one pixel at a time

    - Fill in the large center circle red
    - Fill in the small top circle blue
    - Fill in the square green
    - Fill in the ploygon yellow
    """

    cv2.imshow('Shapes', image)
    cv2.waitKey(0)


def main():
    fill_shapes()

if __name__ == '__main__':
    main()
