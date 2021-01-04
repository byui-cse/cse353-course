"""
File: teach1.py (week 05)

Tasks

- Convert video stream to be grayscale
- Create a circle mask and apply it to the video stream
- Apply a mask file to the video stream
	usa-mask.jpg
	byui-logo.png
- create a vide stream of differences from the camera
	- use gray scale
	- use absdiff() function

"""

"""
Use this code for any of the tasks for the team activity

cap = cv2.VideoCapture(0)  # Notice the '0' instead of a filename
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Wait for 'q' to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

"""

import numpy as np
import cv2


def task0():
    """ Live capture your laptop camera """
    pass


def task1():
	""" 
    Convert video stream to be grayscale and display the live video stream
    """
	pass


def task2():
	""" 
    Create a circle mask and apply it to the live video stream
    """
	pass


def task3():
	""" 
    Apply a mask file 'usa-flag.jpg' to the live video stream
    """
	pass


def task4():
	""" 
    Apply a mask file 'byui-logo.jpg' to the live video stream
    """
	pass


def task5():
	""" 
    create a vide stream of differences from the camera
	- use gray scale images
	- use the OpenCV function absdiff()
    - Questions: are the any methods/techniques to make this work better?
    """
	pass



# ===========================================================
task0()
task1()
task2()
task3()
task4()
task5()
