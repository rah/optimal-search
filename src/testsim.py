#! /usr/env/python
import matplotlib.pyplot as plt
from animate import Animate


def runsim():
    '''
    run a simple simulation of movement
    '''
    mover = Animate()

    for i in range(100):
        mover.move()
        print mover.direction

    x, y = mover.get_movement()
    plt.plot(x, y)
