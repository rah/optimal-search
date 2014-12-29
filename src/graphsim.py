#! /usr/env/python
from random import randint
from environment import Environment
from graphics import GraphWin
from graphics import Point
from graphics import Circle


win = GraphWin("test", 800, 800)
win.setCoords(0, 0, 1000, 1000)

# Set up the environment
env = Environment(1000, 1000, 10)

# create patches
env.create_patches()
for patch in env.patches:
    c = Circle(Point(patch.x_pos, patch.y_pos), patch.radius)
    c.draw(win)

    # Add the entities
    patch.create_entities(randint(0, 10))
    for entity in patch.entities:
        p = Point(entity.x_pos, entity.y_pos)
        p.draw(win)
