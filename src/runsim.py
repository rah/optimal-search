#! /usr/env/python
from environment import Environment
from searcher import Searcher
import graphsim as gs

MAX_MOVES = 50000


def remove_entity(entity):
    patch = entity.parent
    patch.children.remove(entity)


# Set up the environment
env = Environment(1000, 1000, 20)
for patch in env.children:
    patch.create_entities(10)

s = Searcher(x_pos=(env.length / 2.0),
             y_pos=(env.width / 2.0),
             parent=env)

win = gs.setup_graphics_window("test", 800, 800, 1000, 1000)
gs.draw_environment(env, win)

for i in range(MAX_MOVES):
    s.move()

    gs.draw_searcher_move(s, i, win)

    entity = s.detect()
    captured = s.capture(entity)
    if captured is not None:
        gs.undraw_entity(captured, win)
        captured.remove_self()

    if gs.breakout(win):
        break

gs.closewin(win)
