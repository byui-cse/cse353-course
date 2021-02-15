"""
Course: CSE 353
Author: Brother Comeau
File: teach2.py

Instructions:

ta-blocks -> count the number of blocks in the image
ta-cat -> find the eyes only
ta-connect -> count the number of red and yellow circles
ta-maze -> (Hard) find the path through the maze
ta-tiles -> count the number of tiles

"""

import cv2
import numpy as np


# ------------------------------------------------------------------------------------------
def draw_lines(image):
    # Code example from: https://www.geeksforgeeks.org/line-detection-python-opencv-houghline-method/
    # Reading the required image in
    # which operations are to be done.
    # Make sure that the image is in the same
    # directory in which this python program is

    # Convert the img to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection method on the image
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # This returns an array of r and theta values
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

    if (lines is None):
        return image

    # The below for loop runs till r and theta values
    # are in the range of the 2d array
    for r, theta in lines[0]:

        # Stores the value of cos(theta) in a
        a = np.cos(theta)

        # Stores the value of sin(theta) in b
        b = np.sin(theta)

        # x0 stores the value rcos(theta)
        x0 = a*r

        # y0 stores the value rsin(theta)
        y0 = b*r

        # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
        x1 = int(x0 + 1000*(-b))

        # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
        y1 = int(y0 + 1000*(a))

        # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
        x2 = int(x0 - 1000*(-b))

        # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
        y2 = int(y0 - 1000*(a))

        # cv2.line draws a line in image from the point(x1,y1) to (x2,y2).
        # (0,0,255) denotes the colour of the line to be
        #drawn. In this case, it is red.
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    return image

# ------------------------------------------------------------------------------------------
def draw_circles(image):
    # Code from: https://www.geeksforgeeks.org/circle-detection-using-opencv-python
    # Read image.

    # Convert to grayscale.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Blur using 3 * 3 kernel.
    gray_blurred = cv2.blur(gray, (3, 3))

    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(gray_blurred,
                                        cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                                        param2=30, minRadius=1, maxRadius=40)

    # Draw circles that are detected.
    if detected_circles is not None:

        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))

        for a, b, r in detected_circles[0, :]:
            # Draw the circumference of the circle.
            cv2.circle(image, (a, b), r, (0, 255, 0), 2)

            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(image, (a, b), 1, (0, 0, 255), 3)
    
    return image


img = cv2.imread('ta-blocks.jpg')
img = draw_lines(img)
cv2.imshow('lines', img)

img = cv2.imread('ta-cat.jpg')
img = draw_circles(img)
cv2.imshow('circles', img)

cv2.waitKey(0)

