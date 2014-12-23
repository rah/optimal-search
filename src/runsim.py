#! /usr/env/python
import matplotlib.pyplot as plt
from animate import Animate
from searcher import Searcher


def runsim(mover, steps):
    '''
    run a simple simulation of movement
    '''

    for i in range(steps):
        mover.move()
        print mover.direction

    x, y = mover.get_movement()
    plt.plot(x, y)


def run_animate():
    runsim(Animate(), 100)


def run_searcher():
    s = Searcher(90.0, 1.0, 180.0, 0.75, 0.0, 0.0)
    runsim(s, 200)
