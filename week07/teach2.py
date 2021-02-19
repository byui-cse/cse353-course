"""
Course: CSE 353
Author: Brother Comeau
File: teach2.py

Instructions:

As a team, select one of the following 3 tasks

ta-blocks -> count the number of blocks in the image
ta-cat -> find the eyes only
ta-connect -> count the number of red and yellow circles


The following are hard problems to solve.  They are here for you to continue
working on after the team activity

ta-maze -> find the path through the maze
ta-tiles -> count the number of tiles

"""

import cv2
import numpy as np
import math


# ------------------------------------------------------------------------------------------
def draw_lines(image):
    # Convert the img to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection method on the image
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # This returns an array of r and theta values
    lines = cv2.HoughLines(edges, 1, np.pi/180, 50, None, 1, 1)

    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(image, pt1, pt2, (0,0,255), 1, cv2.LINE_AA)

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

img = cv2.imread('ta-connect.png')
img = draw_circles(img)
cv2.imshow('Connect', img)

img = cv2.imread('ta-cat.jpg')
img = draw_circles(img)
cv2.imshow('circles', img)

cv2.waitKey(0)

