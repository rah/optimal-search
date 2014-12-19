#! /usr/env/python
import matplotlib.pyplot as plt
from animate import Animate
from searcher import Searcher


def runsim(clazz=Animate, *args):
    '''
    run a simple simulation of movement
    '''
    mover = clazz(*args)

    for i in range(100):
        mover.move()
        print mover.direction

    x, y = mover.get_movement()
    plt.plot(x, y)


runsim(Animate, 90.0, 1.0, 180.0, 0.75, 0.0, 0.0)
runsim(Searcher, 90.0, 1.0, 180.0, 0.75, 0.0, 0.0, 0)
