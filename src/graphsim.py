#! /usr/env/python
from graphics import GraphWin
from graphics import Point
from graphics import Circle
from graphics import Line


def setup_graphics_window(winname, glength, gwidth, slength, swidth):
        win = GraphWin(winname, glength, gwidth)
        win.setCoords(0, 0, slength, swidth)
        return win


def draw_environment(env, win):
    if win is not None:
        for patch in env.children:
            draw_patch(patch, win)
            for entity in patch.children:
                draw_entity(entity, win)


def draw_patch(patch, win):
    if win is not None:
        c = Circle(Point(patch.x_pos, patch.y_pos), patch.radius)
        c.setOutline("red")
        c.draw(win)


def draw_entity(entity, win):
    if win is not None:
        p = Point(entity.x_pos, entity.y_pos)
        p.setOutline("blue")
        p.draw(win)


def undraw_entity(entity, win):
    if win is not None:
        p = Point(entity.x_pos, entity.y_pos)
        p.setOutline("red")
        p.draw(win)


def draw_searcher_move(s, i, win):
    '''
    For drawing purposes make sure the distace moved
    does not jump from one side of the env to the other
    '''
    if win is not None:
        if (
                abs(s.X[i] - s.X[i+1]) <= s.max_speed and
                abs(s.Y[i] - s.Y[i+1]) <= s.max_speed
        ):
            p = Line(Point(s.X[i], s.Y[i]), Point(s.X[i+1], s.Y[i+1]))
            p.setOutline("green")
            p.draw(win)


def breakout(win):
    if win is not None:
        # Check interaction
        if win.checkKey() == "b":
            return True

    return False


def closewin(win):
    if win is not None:
        if win.getKey() == "c":
            win.close()
            return True

    return False
