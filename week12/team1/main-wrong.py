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
import math

WIDTH = 800
HEIGHT = 800

SQUARE = 1
TRIANGLE = 2

def draw_axis(engine, size):
    for i in range(size):
        engine.dot(i, 0, Red)
        engine.dot(-i, 0, Green)
        engine.dot(0, i, Blue)
        engine.dot(0, -i, Black)

# -----------------------------------------------------------------------------
class Geometry:

    def __init__(self, kind, size):
        super().__init__()
        self.points = []

        self.scale_mat = Matrix3('I')
        self.rotation_mat = Matrix3('I')
        self.trans_mat = Matrix3('I')
        
        half = size // 2

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


    def add_point(self, x, y):
        """ Add a point to the geometry """
        self.points.append(Point(x, y))


    def scale(self, sx, sy):
        """ set the scale of the object """
        self.scale_mat.scale(sx, sy)


    def rotation(self, rot):
        """ set the rotation (degress) of the object """
        self.rotation_mat.rotation(rot)


    def translate(self, dx, dy):
        """ set to translation of the object """
        self.trans_mat.translation(dx, dy)


    def _createTRS(self):
        return (self.trans_mat * self.rotation_mat * self.scale_mat)


    def draw(self, engine):
        """ draw all of the points using the engine "draw_dot()" """
        trs = self._createTRS()
        # for i in range(len(self.points) - 1):
        #     engine.draw_line(self.points[i], self.points[i + 1], trs)

        for i in range(len(self.points) - 1):
            p1 = self.points[i] * trs
            p2 = self.points[i + 1] * trs
            points = self._plotLine(p1.getX(), p1.getY(), p2.getX(), p2.getY())
            for pt in points:
                engine.dot(pt.getX(), pt.getY())


    def _plotLine(self, x0, y0, x1, y1):
        if math.fabs(y1 - y0) < math.fabs(x1 - x0):
            if x0 > x1:
                return self._plotLineLow(x1, y1, x0, y0)
            else:
                return self._plotLineLow(x0, y0, x1, y1)
        else:
            if y0 > y1:
                return self._plotLineHigh(x1, y1, x0, y0)
            else:
                return self._plotLineHigh(x0, y0, x1, y1)

    def _plotLineLow(self, x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0
        yi = 1
        if dy < 0:
            yi = -1
            dy = -dy

        D = 2*dy - dx
        y = y0

        points = []
        for x in frange(x0, x1):
            points.append(Point(x, y))
            if D > 0:
                y = y + yi
                D = D - 2*dx
            D = D + 2*dy
        return points


    def _plotLineHigh(self, x0,y0, x1,y1):
        dx = x1 - x0
        dy = y1 - y0
        xi = 1
        if dx < 0:
            xi = -1
            dx = -dx
        D = 2*dx - dy
        x = x0

        points = []
        for y in frange(y0, y1):
            points.append(Point(x, y))
            if D > 0:
                x = x + xi
                D = D - 2*dy
            D = D + 2*dx
        return points


# -----------------------------------------------------------------------------
def testing(engine):
    square1 = Geometry(SQUARE, 50)
    square1.translate(100, 100)
    square1.scale(0.5, 1.0)

    square2 = Geometry(SQUARE, 100)
    square2.translate(-100, 100)
    square2.scale(0.5, 1.0)

    square3 = Geometry(SQUARE, 50)
    square3.translate(-100, -100)
    square3.scale(1.5, 0.2)

    triangle1 = Geometry(TRIANGLE, 50)
    triangle1.translate(100, -100)

    times = 3
    step = 2
    world_rot = 0
    world_scale = 1
    for rot in range(0, 360 * times + step, step):
        engine.clear()
        draw_axis(engine, 150)

        square1.rotation(rot)

        square2.rotation(-rot * 2)

        square3.scale(rot / 360, 1)
        square3.rotation(rot)

        triangle1.rotation(-rot)
        triangle1.scale(rot / 360, rot / 360)

        # draw all
        square1.draw(engine)
        square2.draw(engine)
        square3.draw(engine)
        triangle1.draw(engine)

        # TODO - Uncomment these lines after you have the objects drawn correctly
        world_rot += step / times
        engine.rotation(world_rot)
        world_scale += 0.002
        engine.scale(world_scale, 1.0)

        engine.display()
        engine.wait(1)

    pass

# -----------------------------------------------------------------------------
def main():
    engine = Engine("test - Press any key to close", WIDTH, HEIGHT)

    """
    TODO

    Geometry Class

    1) Impliment the class Geometry methods.

    Engine

    2) currently, every time the engine draws a point on the screen, it
       creates the TRS matrix.  Change the engine to only create this matrix
       when the scale, rotation, or translate methods are called.

    3) Create a new engine method called draw_dot() that has the arguments:
        - x 
        - y
        - TRS martix of an object
        - color='000000'

       This new method will take the argument TRS and also use the engine's TRS
       to draw the dot on the screen.

    4) Uncomment the lines in the testing() function for changing the world matrix
       after you have the objects drawing

    5) Question: in your final screen of the program, the lines for squares and
      triangles are not solid.  How could you change your program to keep these
      lines solid?
    """

    # Set world space
    # Move all drawing to center of the window.  Make center (0, 0)
    engine.translate(WIDTH / 2, HEIGHT / 2)

    # rotation world 30 degrees
    # engine.rotation(30)

    # scale world
    # engine.scale(2, 2)

    # the axis should be rotated 30 degrees, in the center and double the size
    draw_axis(engine, 150)

    testing(engine)

    engine.display()
    engine.wait(0)
    engine.close()


if __name__ == '__main__':
    main()
