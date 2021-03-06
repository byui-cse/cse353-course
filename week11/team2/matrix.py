"""
Course: CSE 353
Lesson Week: 11
File: matrix.py
Author: Brother Comeau
Purpose: matrix class
"""
import math
from common import *

# ----------------------------------------------------------------------------
# Matrix class
# This class is used by some of the method in Crush
class Matrix3:

    def __init__(self, mat_type='I', b=None, c=None):

        self.mat = [[0.0 for x in range(3)] for y in range(3)]

        if (mat_type == 'E'):
            pass
        elif (mat_type == 'I'):
            self.setIdent()
        elif (mat_type == 'S'):
            self.setScale(float(b), float(c))
        elif (mat_type == 'R'):
            self.setRotation(float(b))
        elif (mat_type == 'T'):
            self.setScale(float(b), float(c))
        else:
            self.setIdent()


    def __repr__(self):
        str1 = f"|{self.mat[0][0]:10.2f} {self.mat[0][1]:10.2f} {self.mat[0][2]:10.2f}|\n"
        str2 = f"|{self.mat[1][0]:10.2f} {self.mat[1][1]:10.2f} {self.mat[1][2]:10.2f}|\n"
        str3 = f"|{self.mat[2][0]:10.2f} {self.mat[2][1]:10.2f} {self.mat[2][2]:10.2f}|\n"
        line = '----------------------------------'
        return line + '\n' + str1 + str2 + str3 + line


    def setIdent(self):
        self.setMatrix([1,0,0,0,1,0,0,0,1])


    def setMatrix(self, values):
        self.mat[0][0] = float(values[0])
        self.mat[0][1] = float(values[1])
        self.mat[0][2] = float(values[2])
        self.mat[1][0] = float(values[3])
        self.mat[1][1] = float(values[4])
        self.mat[1][2] = float(values[5])
        self.mat[2][0] = float(values[6])
        self.mat[2][1] = float(values[7])
        self.mat[2][2] = float(values[8])


    def scale(self, scalex, scaley):
        self.mat[0][0] = float(scalex)
        self.mat[0][1] = float(0)

        self.mat[1][0] = float(0)
        self.mat[1][1] = float(scaley)

        self.mat[2][0] = float(0)
        self.mat[2][1] = float(0)
        self.mat[2][2] = float(1)


    def rotation(self, rotation):
        rads = deg2rad(rotation)
        self.mat[0][0] = float(math.cos(rads))
        self.mat[0][1] = float(-math.sin(rads))

        self.mat[1][0] = float(math.sin(rads))
        self.mat[1][1] = float(math.cos(rads))

        self.mat[2][0] = float(0)
        self.mat[2][1] = float(0)
        self.mat[2][2] = float(1)


    def translation(self, dx, dy):
        self.mat[0][2] = float(dx)
        self.mat[1][2] = float(dy)


    # Return the results of A * B
    def __mul__(self, other):
        tmp = Matrix3('E')
        # for r in range(3):
        #     for c in range(3):
        #         for k in range(3):
        #             tmp.mat[r][c] += self.mat[r][k] * other.mat[k][c]
        # return tmp
        tmp.mat[0][0] = (self.mat[0][0] * other.mat[0][0]) + (self.mat[0][1] * other.mat[1][0]) + (self.mat[0][2] * other.mat[2][0])
        tmp.mat[1][0] = (self.mat[1][0] * other.mat[0][0]) + (self.mat[1][1] * other.mat[1][0]) + (self.mat[1][2] * other.mat[2][0])
        tmp.mat[2][0] = (self.mat[2][0] * other.mat[0][0]) + (self.mat[2][1] * other.mat[1][0]) + (self.mat[2][2] * other.mat[2][0])

        tmp.mat[0][1] = (self.mat[0][0] * other.mat[0][1]) + (self.mat[0][1] * other.mat[1][1]) + (self.mat[0][2] * other.mat[2][1])
        tmp.mat[1][1] = (self.mat[1][0] * other.mat[0][1]) + (self.mat[1][1] * other.mat[1][1]) + (self.mat[1][2] * other.mat[2][1])
        tmp.mat[2][1] = (self.mat[2][0] * other.mat[0][1]) + (self.mat[2][1] * other.mat[1][1]) + (self.mat[2][2] * other.mat[2][1])

        tmp.mat[0][2] = (self.mat[0][0] * other.mat[0][2]) + (self.mat[0][1] * other.mat[1][2]) + (self.mat[0][2] * other.mat[2][2])
        tmp.mat[1][2] = (self.mat[1][0] * other.mat[0][2]) + (self.mat[1][1] * other.mat[1][2]) + (self.mat[1][2] * other.mat[2][2])
        tmp.mat[2][2] = (self.mat[2][0] * other.mat[0][2]) + (self.mat[2][1] * other.mat[1][2]) + (self.mat[2][2] * other.mat[2][2])

        return tmp

    # Return the results of A + B
    def __add__(self, other):
        tmp = Matrix3('E')
        for r in range(3):
            for c in range(3):
                tmp.mat[r][c] = self.mat[r][c] + other.mat[r][c]
        return tmp


    # Return the results of A - B
    def __sub__(self, other):
        tmp = Matrix3('E')
        for r in range(3):
            for c in range(3):
                tmp.mat[r][c] = self.mat[r][c] - other.mat[r][c]
        return tmp
