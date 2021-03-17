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

def draw_axis(engine, size):
    for i in range(size):
        engine.dot(i, 0, Red)
        engine.dot(-i, 0, Green)
        engine.dot(0, i, Blue)
        engine.dot(0, -i, Black)


# ----------------------------------------------------------------------------
def test1(engine):
    # This is object space that you are setting
    engine.translate(50, -150)

    # The positions are object based (0, 0) is NOT in the center of the window
    for i in range(100):
        engine.dot(i, 0)
        engine.dot(0, i)
        engine.dot(i, 100)
        engine.dot(100, i)


# ----------------------------------------------------------------------------
def test2(engine):
    # This is object space that you are setting
    engine.translate(-150, -150)
    engine.rotation(-30)

    # The positions are object based (0, 0) is NOT in the center of the window
    for i in range(100):
        engine.dot(i, 0)
        engine.dot(0, i)
        engine.dot(i, 100)
        engine.dot(100, i)


# ----------------------------------------------------------------------------
def test3(engine):
    # This is object space that you are setting
    engine.translate(50, 150)
    engine.rotation(-30)
    engine.scale(0.5, 0.75)

    # The positions are object based (0, 0) is NOT in the center of the window
    for i in range(100):
        engine.dot(i, 0)
        engine.dot(0, i)
        engine.dot(i, 100)
        engine.dot(100, i)

def main():
    engine = Engine("test - Press any key to close", WIDTH, HEIGHT)

    """
    TODO

    There already exists these functions in the engine.  The idea with these function is 
    that they can be called many times while drawing.  Currently, they effect all drawing
    commands after you change the rotation, scale and translation.  However, think of them
    more as matrices for an object.
        - rotation(rot):
        - scale(x, y):
        - translate(x, y):

    Add engine scale and rotation like the world_offset() method.
    These functions will apply to world space of the drawing

    Read the following article and implement "world space" in the engine
    http://findnerd.com/list/view/Computer-Graphics-Different-Spaces/6982/

    You will be creating:
        world_rotation(rot)
        world_scale(x, y)

    """

    # Set world space
    
    # Move all drawing to center of the window.  Make center (0, 0)
    engine.world_offset(WIDTH / 2, HEIGHT / 2)

    # rotation world 30 degrees
    engine.world_rotation(30)

    # scale world
    engine.world_scale(2, 2)

    # the axis should be rotated 30 degrees, in the center and double the size
    draw_axis(engine, 150)

    test1(engine)
    test2(engine)
    test3(engine)

    engine.display()
    engine.wait(0)
    engine.close()


if __name__ == '__main__':
    main()
