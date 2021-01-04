"""
Course: CS312
File: teach1.py
Description:
   OpenCV functions

   You are NOT submitting this program.
"""

"""
Instructions:

- You will impliementing the following functions using Opencv
- The first step is to make sure that you have OpenCV for Python installed
- You a free to use any images for the function below (except task 5)
  - Download images from the Internet
  - Use your own photos
- You must download "temple.jpg" and "usa.png" from the GitHub repo for task 5

"""
import numpy as np
import cv2


def task1(file):
    """ task1: load and display an image """
    print('Task 1')



def task2(file):
    """ Task2: Open image and flip left <-> right """
    print('Task 2')



def task3(file):
    """ Task3: Open image and flip up <-> down """
    print('Task 3')



def task4(file):
    """ Task4: Resample image down 50% """
    print('Task 4')



def task5():
    """ Task5: Tile a small image into a larger one """
    print('Task 5')



def task6():
    """ Task6: EXTRA - Tile a small image into a larger one like a brick wall """
    # load file and create a large 400 x 600 tiled image
    print('Task 6')



def main():
    """ Main function """

    # Main image file to use for the first 4 tasks
    file = 'temple.jpg'

    task1(file)
    task2(file)
    task3(file)
    task4(file)
    task5()
    task6()


if __name__ == "__main__":
    # execute only if run as a script
    main()
