#! /usr/env/python
from math import cos, sin, radians

import random
import matplotlib.pyplot as plt


def relMove(direction, distance):
    '''
    return the relative x, y coordinates give direction and distance
    '''
    x = distance * cos(radians(direction))
    y = distance * sin(radians(direction))

    return x, y


def angle_turned():
    max_turn = 30.0
    turn = max_turn * random.random()

    if random.random() > 0.5:
        return -(turn)
    else:
        return turn


def distance_moved(speed):
    return random.random() * speed


def runsim():
    '''
    run a simple simulation of movement
    '''
    # Set initial location
    X = 0.0
    Y = 0.0

    # Set initial direction and speed
    direction = 0.0
    speed = 1.0

    x_plt = []
    y_plt = []

    for i in range(100):
        direction += angle_turned()
        distance = distance_moved(speed)

        x, y = relMove(direction, distance)

        X += x
        Y += y

        x_plt.append(X)
        y_plt.append(Y)

        plt.plot(x_plt, y_plt)

