#! /usr/env/python
from math import cos, sin, radians


def relMove(direction, speed):
    '''
    return the relative x, y coordinates give direction and speed
    '''
    x = speed * cos(radians(direction))
    y = speed * sin(radians(direction))

    return x, y
