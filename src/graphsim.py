#! /usr/env/python
from environment import Environment
from searcher import Searcher
from graphics import GraphWin
from graphics import Point
from graphics import Circle
from graphics import Line

MAX_MOVES = 50000
GRAPHICS = True

def draw_patches(env, win):
    for patch in env.children:
        draw_patch(patch, win)
        for entity in patch.children:
            draw_entity(entity, win)


def draw_patch(patch, win):
    c = Circle(Point(patch.x_pos, patch.y_pos), patch.radius)
    c.setOutline("red")
    c.draw(win)


def draw_entity(entity, win):
    p = Point(entity.x_pos, entity.y_pos)
    p.setOutline("blue")
    p.draw(win)


def undraw_entity(entity, win):
    p = Point(entity.x_pos, entity.y_pos)
    p.setOutline("red")
    p.draw(win)


def draw_searcher_move(s, i, win):
    '''
    For drawing purposes make sure the distace moved
    does not jump from one side of the env to the other
    '''
    if (
            abs(s.X[i] - s.X[i+1]) <= s.max_speed and
            abs(s.Y[i] - s.Y[i+1]) <= s.max_speed
    ):
        p = Line(Point(s.X[i], s.Y[i]), Point(s.X[i+1], s.Y[i+1]))
        p.setOutline("green")
        p.draw(win)


def remove_entity(entity, win):
    patch = entity.parent
    patch.children.remove(entity)

if GRAPHICS:
    win = GraphWin("test", 800, 800)
    win.setCoords(0, 0, 1000, 1000)

# Set up the environment
env = Environment(1000, 1000, 20)
for patch in env.children:
    patch.create_entities(10)

if GRAPHICS:
    draw_patches(env, win)

s = Searcher(x_pos=(env.length / 2.0),
             y_pos=(env.width / 2.0),
             parent=env)

i = 0
while (i < MAX_MOVES):
    s.move()

    if GRAPHICS:
        draw_searcher_move(s, i, win)

    entity = s.detect()
    captured = s.capture(entity)
    if captured is not None:
        if GRAPHICS:
            undraw_entity(captured, win)
        remove_entity(captured, win)

    i += 1

    if GRAPHICS:
        # Check interaction
        key = win.checkKey()
        if key == "p":
            if win.getKey() == "s":
                break
            else:
                continue
        elif key == "s":
            break

if GRAPHICS:
    if win.getKey() == "c":
        win.close()
