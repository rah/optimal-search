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


def draw_patches(env, win):
    for patch in env.children:
        # Draw the patch
        c = Circle(Point(patch.x_pos, patch.y_pos), patch.radius)
        c.setOutline("red")
        c.draw(win)

        # Draw the entities in the patch
        for entity in patch.children:
            p = Point(entity.x_pos, entity.y_pos)
            p.setOutline("blue")
            p.draw(win)


def draw_searcher_move(s, i, win):
        p = Line(Point(s.X[i], s.Y[i]), Point(s.X[i+1], s.Y[i+1]))
        p.setOutline("green")
        p.draw(win)


def remove_entity(entity):
    pass


win = GraphWin("test", 800, 800)
win.setCoords(0, 0, 1000, 1000)

# Set up the environment
env = Environment(1000, 1000, 10)
for patch in env.children:
    patch.create_entities(10)
    
draw_patches(env, win)

x = random() * env.length
y = random() * env.width
s = Searcher(x_pos=x, y_pos=y, parent=env)

i = 0
while (i < MAX_MOVES):
    s.move()
    draw_searcher_move(s, i, win)

    entity = s.capture()
    if entity is not None:
        remove_entity(entity)

    i += 1

    # Check interaction
    key = win.checkKey()
    if key == "p":
        if win.getKey() == "s":
            break
        else:
            continue
    elif key == "s":
        break

if win.getKey() == "c":
    win.close()
