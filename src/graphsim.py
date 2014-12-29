#! /usr/env/python
from random import randint
from random import random
from environment import Environment
from searcher import Searcher
from graphics import GraphWin
from graphics import Point
from graphics import Circle
from graphics import Line

MAX_MOVES = 50000


def check_and_set_bounds(env, searcher):
    if searcher.curr_x <= 0.0:
        searcher.setx(env.length - 1.0)
        return True
    if searcher.curr_x >= env.length:
        searcher.setx(0.0 + 1.0)
        return True
    if searcher.curr_y <= 0.0:
        searcher.sety(env.width - 1.0)
        return True
    if searcher.curr_y >= env.width:
        searcher.sety(0.0 + 1.0)
        return True

    return False

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

i = 0
while (i < MAX_MOVES):
    s.move()

    if not check_and_set_bounds(env, s):
        p = Line(Point(s.X[i], s.Y[i]), Point(s.X[i+1], s.Y[i+1]))
        p.setOutline("green")
        p.draw(win)

    i += 1
    if win.checkMouse() is not None:
        break

if win.getKey() == "k":
    win.close()
