"""
Course: CSE 353
File: teach1.py
Description:
   OpenCV functions

   You are NOT submitting this program.
"""

"""
Instructions:

- You will implementing the following functions
- You must download the image files from Github for week04:

    byuisign.jpg
    greenscreen.jpg
    team1-image1.jpg
    team1-image2.jpg

"""

import numpy as np
import cv2


# ----------------------------------------------------------------------------
def blend():
    """ Blend two images together and display the results 
        Use loops not OpenCV functions
    """

    # TODO - load team1-image1.jpg and team1-image2.jpg
    image1 = cv2.imread('team1-image1.jpg')
    image2 = cv2.imread('team1-image2.jpg')


    # TODO - Task 1) blend these images together in an even gradient

    # TODO - Task 2) blend these images together any way you want (be creative)


# ----------------------------------------------------------------------------
def green_screen():
    """ Place one image in another using green screen (don't use masking in OpenCV) 
        Display the results.
        Use loops not OpenCV functions
    """

    # TODO - load byuisign.jpg and greenscreen.jpg
    sign = cv2.imread('byuisign.jpg')
    green = cv2.imread('greenscreen.jpg')

    # TODO - Place the greenscreen on the byui sign image with the green 
    #        (you decide where on the sign image)


# ----------------------------------------------------------------------------
def main():
    blend()
    green_screen()

if __name__ == '__main__':
    main()

