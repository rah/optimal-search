#! /usr/env/python
from random import randint
from random import random
from environment import Environment
from searcher import Searcher
from graphics import GraphWin
from graphics import Point
from graphics import Circle
from graphics import Line


win = GraphWin("test", 800, 800)
win.setCoords(0, 0, 1000, 1000)

# Set up the environment
env = Environment(1000, 1000, 10)

# create patches
env.create_patches()
for patch in env.patches:
    c = Circle(Point(patch.x_pos, patch.y_pos), patch.radius)
    c.setOutline("red")
    c.draw(win)

    # Add the entities
    patch.create_entities(randint(0, 10))
    for entity in patch.entities:
        p = Point(entity.x_pos, entity.y_pos)
        p.setOutline("blue")
        p.draw(win)

x = random() * env.length
y = random() * env.width
s = Searcher(x_pos=x, y_pos=y)

for i in range(10000):
    s.move()
    p = Line(Point(s.X[i], s.Y[i]), Point(s.X[i+1], s.Y[i+1]))
    p.setOutline("green")
    p.draw(win)
