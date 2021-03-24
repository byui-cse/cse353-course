"""
Course: CSE 353
Lesson Week: 11
File: main.py
Author: Brother Comeau
Purpose: main program for test1 the engine
"""

# Import the graphics code that will allow us to draw in a window
from engine import *
from matrix import *
from point import *
import math

WIDTH = 800
HEIGHT = 800

SQUARE = 1
TRIANGLE = 2
CIRCLE = 3

def draw_axis(engine, size):
    engine.draw_line(Point(-size, 0), Point(size, 0), None)
    engine.draw_line(Point(0, -size), Point(0, size), None)

# -----------------------------------------------------------------------------
class Geometry:

    def __init__(self, kind, size, color='000000'):
        super().__init__()
        self.points = []

        self.scale_mat = Matrix3('I')
        self.rotation_mat = Matrix3('I')
        self.trans_mat = Matrix3('I')
        self.color = color 
        self.children = []

        half = size // 2
        
        self.trs = self._createTRS()

        if kind == SQUARE:
            self.points.append(Point(-half, -half))
            self.points.append(Point(half, -half))
            self.points.append(Point(half, half))
            self.points.append(Point(-half, half))
            self.points.append(Point(-half, -half))

        elif kind == TRIANGLE:
            x1 = math.sin(deg2rad(30)) * half
            y1 = math.cos(deg2rad(30)) * half
            x2 = math.sin(deg2rad(150)) * half
            y2 = math.cos(deg2rad(150)) * half
            x3 = math.sin(deg2rad(270)) * half
            y3 = math.cos(deg2rad(270)) * half

            self.points.append(Point(x1, y1))
            self.points.append(Point(x2, y2))
            self.points.append(Point(x3, y3))
            self.points.append(Point(x1, y1))

        elif kind == CIRCLE:
            step = 6
            for i in range(0, 360 + step, step):
                pt = Point(-math.cos(deg2rad(i)) * size, math.sin(deg2rad(i)) * size)
                self.points.append(pt)
   

    def add_child(self, geometry):
        self.children.append(geometry)


    def add_point(self, x, y):
        """ Add a point to the geometry """
        self.points.append(Point(x, y))


    def scale(self, sx, sy):
        """ set the scale of the object """
        self.scale_mat.scale(sx, sy)
        self.trs = self._createTRS()


    def rotation(self, rot):
        """ set the rotation (degress) of the object """
        self.rotation_mat.rotation(rot)
        self.trs = self._createTRS()


    def translate(self, dx, dy):
        """ set to translation of the object """
        self.trans_mat.translation(dx, dy)
        self.trs = self._createTRS()


    def _createTRS(self):
        return (self.trans_mat * self.rotation_mat * self.scale_mat)


    def draw(self, engine):
        for i in range(len(self.points) - 1):
            engine.draw_line(self.points[i], self.points[i + 1], self.trs, self.color)
       


def test2(engine):
    # Sun
    sun = Geometry(CIRCLE, 40, color='ff0000')
    sun.translate(0, 0)
    sun.draw(engine)

    # Earth
    earth = Geometry(CIRCLE, 10, color='00ff00')
    earth.translate(0, 0)
    earth.draw(engine)

    # Moon
    moon = Geometry(CIRCLE, 3, color='0000ff')
    moon.translate(0, 0)
    moon.draw(engine)

    # create parent / child relationships
    sun.add_child(earth)
    earth.add_child(moon)

    step = 1
    times = 2
    sun_dist = 10
    earth_dist = 100
    moon_dist = 20
    for rot in range(0, 360 * times + step, step):

        engine.clear()
        draw_axis(engine, 150)

        # Position the sun
        pos_x = -math.cos(deg2rad(rot * 6)) * sun_dist
        pos_y = math.sin(deg2rad(rot * 6)) * sun_dist
        sun.translate(pos_x, pos_y)

        # Position the earth
        pos_x = -math.cos(deg2rad(rot)) * earth_dist
        pos_y = math.sin(deg2rad(rot)) * earth_dist
        earth.translate(pos_x, pos_y)

        pos_x = -math.cos(deg2rad(rot * 10)) * moon_dist
        pos_y = math.sin(deg2rad(rot * 10)) * moon_dist
        moon.translate(pos_x, pos_y)

        sun.draw(engine)

        # this is just for testing,  draw the sun should draw earth and moon
        # earth.draw(engine)
        # moon.draw(engine)

        engine.display()
        engine.wait(10)

# -----------------------------------------------------------------------------
def main():
    engine = Engine("test2 - Press any key to close", WIDTH, HEIGHT)

    """
    TODO
    Geometry Class

    - Get the sun (and it's children) to draw correctly
    """

    # Set world space
    # Move all drawing to center of the window.  Make center (0, 0)
    engine.translate(WIDTH / 2, HEIGHT / 2)
    engine.scale(1.5, 1.5)

    draw_axis(engine, 150)

    # test1(engine)
    test2(engine)

    engine.display()
    engine.wait(0)
    engine.close()


if __name__ == '__main__':
    main()
