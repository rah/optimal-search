#! /usr/env/python
import sys

from environment import Environment

sys.path.append("c:/Users/Ross/workspace/graphics")
from graphics import GraphWin
from graphics import Point
from graphics import Circle


win = GraphWin("test", 800, 600)
win.setCoords(0, 0, 1000, 1000)

env = Environment(1000, 1000, 10)
env.create_patches()

patches = env.patches

for patch in patches:
    # print patch.x_pos, patch.y_pos, patch.radius
    c = Circle(Point(patch.x_pos, patch.y_pos), patch.radius)
    c.draw(win)
