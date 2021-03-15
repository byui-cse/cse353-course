"""
Course: CSE 353
Lesson Week: 11
File: main.py
Author: Brother Comeau
Purpose: main program for testing the engine
"""

# Import the graphics code that will allow us to draw in a window
from engine import *
from matrix import *
from point import *

WIDTH = 800
HEIGHT = 800

def draw_axis(engine):

    axis = 300
    for i in range(axis):
        engine.dot(i, 0, 'red')
        engine.dot(-i, 0, 'green')
        engine.dot(0, i, 'blue')
        engine.dot(0, -i, 'black')


def translate(engine):

    # TODO - Draw square (-50, -50, 50, 50)

    # TODO - translate the square by (10, 20)
    pass


def rotation(engine):

    # TODO - Draw square (-50, -50, 50, 50)

    # TODO - rotate the square by 30 degrees
    pass


def scale(engine):
    # TODO - Draw square (-50, -50, 50, 50)

    # TODO - scale square by 2x
    pass


def main():

    # TODO - Move all drawing to center of the window.  Make center (0, 0)

    engine = Engine("test - Click in window to close", WIDTH, HEIGHT)

    draw_axis(engine)

    # translate(engine)
    # rotation(engine)
    # scale(engine)

    engine.getMouse() # pause for click in window
    engine.close()


if __name__ == '__main__':
    main()
