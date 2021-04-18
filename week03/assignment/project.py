"""
Course: CSE 353
File: project03.py
Description: 

    Using OpenCV

    You are submitting this project to Canvas when completed.
    Only your project code must be submitted.  Do NOT submit the
    testing code file testfunctions.py

    Read the requirements for the project in Canvas
"""

import numpy as np
import cv2
import testfunctions
import os
from os import path


def convert_image(srcfilename, dstfilename):
    """ Convert an image to a different file format """
    pass


def resize_image(srcfilename, dstfilename, scale):
    """ Resize image
        if scale is < 100.0, remove rows and cols
        if scale is > 100.0, set new rows and cols to (0, 0, 0)
        Can't use any resizing functions in OpenCV
    """	
    pass


def border_image(srcfilename, dstfilename, width, color):
    """ Add a border to an image
        Can't use any border functions in OpenCV
    """
    pass


def create_mondrian():
    """ Create your own Mondrian image 
        Your image must at least 200 x 300 - you can create an image larger
        This function must save the results to to given filename

        https://www.youtube.com/watch?v=xkq5jQhH0WE

    """

    # This line is only here for testing, keep, change or delete it
    image = np.zeros((400, 600), dtype=np.uint8)

    # These lines are used for displaying the finished image.  Do not remove
    cv2.imshow('Mondrian', image)
    cv2.waitKey(0)



def main():
    """ Main function """

    # Do NOT modify anything below.  You can comment out functions while
    # working on your project.  However, you must restore it to the below code

    tests = testfunctions.Tests(__file__)

    # Convert images
    tests.test1(convert_image)
    tests.test2(convert_image)
    tests.test3(convert_image)

    # Resize
    tests.test4(resize_image, 100)
    tests.test4(resize_image, 50)
    tests.test4(resize_image, 124)

    # border
    tests.test5(border_image, 5, (128, 128, 128))
    tests.test5(border_image, 20, (0, 255, 255))
   
    tests.finished()

    # Make it your own
    create_mondrian()


if __name__ == "__main__":
    # execute only if run as a script
    main()
