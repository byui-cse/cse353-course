"""
Course: CSE 353
Lesson Week: 02
File: team2.py
Author: Brother Comeau
Instructions:

- Install matplotlib
    ".....\python.exe -m pip install matplotlib"

- review function sample() to understand how to create an image that
  can be changed and displayed.

- Implement part1(), part2() and part3() 

"""

from matplotlib import pyplot as plt
import numpy as np
import random
import math

# Colors
RED = [255, 0, 0]
BLUE = [0, 0 ,255]
GREEN = [0, 255, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

# ----------------------------------------------------------------------------
def display_np(array, title=''):
    plt.title(title)
    plt.imshow(array, interpolation='nearest')
    plt.show()


# ----------------------------------------------------------------------------
def set_pixel(array, x, y, color):
    array[x, y] = color


# ----------------------------------------------------------------------------
def sample():
    # create a black 500 x 500 array, 3 colors deep -> [R, G, B]
    data = np.zeros( (500, 500, 3), dtype=np.uint8)

    # set top left corner to red [255, 0, 0]
    data[0:100, 0:100] = RED
    
    # display the array in a plot
    display_np(data, title='Red square top left')



# ----------------------------------------------------------------------------
def part1(width, height, size, color):
    """
    Create an image of size (w x h) and color a square in the center
    of size "size" and color "color".  Display the image at the end.
    """
    pass

# ----------------------------------------------------------------------------
def part2(width, height):
    """
        Using colors red, white and blue, create a US flag of size (w x h).
        Don't need to draw the stars.
    """
    pass

# ----------------------------------------------------------------------------
def plotLineLow(array, x0, y0, x1, y1):
    pass

def plotLineHigh(array, x0, y0, x1, y1):
    pass

def plotLine(array, x0, y0, x1, y1, color):
    pass

def part3(width, height):
    """
        Implement Bresenham's line algorithm
        https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

        You will be implementing the following three functions found above.
        
        plotLineLow(x0, y0, x1, y1)
        plotLineHigh(x0, y0, x1, y1)
        plotLine(x0, y0, x1, y1)

        replace "plot(x, y)" with set_pixel() found in this file.
    """

    # TODO create a "black" array of size width x height x 3 (Change array below)
    array = None

    # TODO draw lines
    if array != None:
        for i in range(100):
            # random start and end points
            x0 = random.randint(0, width)
            y0 = random.randint(0, height)
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)

            # create random color
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

            # draw a line
            plotLine(array, x0, y0, x1, y1, color)

        display_np(array)



def main():
    sample()        # Comment out after looking at the function

    part1(400, 500, 100, RED)
    part2(400, int(300 * 1.9))
    part3(500, 600)


if __name__ == '__main__':
    main()