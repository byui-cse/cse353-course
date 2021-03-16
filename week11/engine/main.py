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
        engine.dot(i, 0, Red)
        engine.dot(-i, 0, Green)
        engine.dot(0, i, Blue)
        engine.dot(0, -i, Black)


def translate(engine):

    # TODO - Draw square (-50, -50, 50, 50)
    for i in range(10):
        engine.dot(-50 + i, -50)
        engine.dot(-50 + i, 50)
        engine.dot(50 + i, -50)
        engine.dot(50 + i, 50)

    engine.translate(100, -90)

    # TODO - Draw square (-50, -50, 50, 50)
    for i in range(10):
        engine.dot(-50 + i, -50)
        engine.dot(-50 + i, 50)
        engine.dot(50 + i, -50)
        engine.dot(50 + i, 50)

    # TODO - translate the square by (10, 20)


def rotation(engine):

    engine.translate(-250, -100)
    for angle in range(0, 361, 30):
        engine.rotation(angle)

        # TODO - Draw square (-50, -50, 50, 50)
        for i in range(40):
            engine.dot(-50 + i, -50)
            engine.dot(-50 + i, 50)
            engine.dot(50 + i, -50)
            engine.dot(50 + i, 50)

        engine.display()
        engine.wait(10)

    # TODO - rotate the square by 30 degrees


def scale(engine):
    # TODO - Draw square (-50, -50, 50, 50)

    engine.translate(0, 0)
    for i in range(60):
        engine.dot(-50 + i, -50, Red)
        engine.dot(-50 + i, 50, Red)
        engine.dot(50 + i, -50, Red)
        engine.dot(50 + i, 50, Red)


    engine.scale(1.5, 3.5)

    for i in range(60):
        engine.dot(-50 + i, -50, Blue)
        engine.dot(-50 + i, 50, Blue)
        engine.dot(50 + i, -50, Blue)
        engine.dot(50 + i, 50, Blue)

    # TODO - scale square by 2x


def main():

    # TODO - Move all drawing to center of the window.  Make center (0, 0)

    engine = Engine("test - Press any key to close", WIDTH, HEIGHT)

    engine.set_offset(WIDTH / 2, HEIGHT / 2)

    draw_axis(engine)

    translate(engine)
    rotation(engine)
    scale(engine)

    engine.display()
    engine.wait(0)
    engine.close()


if __name__ == '__main__':
    main()
