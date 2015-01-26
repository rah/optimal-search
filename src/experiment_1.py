#! /usr/env/python
"""
Experiment 1: Examine the impact of changing the number of entities
              on the default parameters of the searcher.
"""
from environment import Environment
from searcher import Searcher

ENV_SIZE = 1000
N_PATCHES = 20
N_ENTITIES_PER_PATCH = 10

MAX_MOVES = 50000

N_TRIALS = 20

for trail in range(N_TRIALS):
    # Set up the environment
    env = Environment(ENV_SIZE, ENV_SIZE, N_PATCHES)
    for patch in env.children:
        patch.create_entities(N_ENTITIES_PER_PATCH)

    s = Searcher(x_pos=(env.length / 2.0),
                 y_pos=(env.width / 2.0),
                 parent=env)

    for i in range(MAX_MOVES):
        s.move()
        entity = s.detect()
        s.capture(entity)

    print("Total entities captured = ", len(s.captured))
