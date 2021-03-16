"""
Course: CSE 353
Lesson Week: 11
File: common.py
Author: Brother Comeau
Purpose: Common functions for engine
"""

import math

Black = "000000"
Green = "008000"
Silver = "C0C0C0"
Lime = "00FF00"
Gray = "808080"
Olive = "808000"
White = "FFFFFF"
ellow = "FFFF00"
Maroon = "800000"
Navy = "000080"
Red = "FF0000"
Blue = "0000FF"
Purple = "800080"
Teal = "008080"
Fuchsia = "FF00FF"
Aqua = "00FFFF"


def color_rgb(r,g,b):
    """r,g,b are intensities of red, green, and blue in range(256)
    Returns color specifier string for the resulting color"""
    return "#%02x%02x%02x" % (r,g,b)


def colorname_to_rgb(name):
    # print(name)
    return (int(name[4:6], 16), int(name[2:4], 16), int(name[0:2], 16))


def deg2rad(value):
    return (((math.pi / 180.0) * (value)))


def rad2deg(value):
    return (((value) * (180.0 / math.pi)))


def frange(x, y, jump = 1.0):
    while x < y:
        yield x
        x += jump

