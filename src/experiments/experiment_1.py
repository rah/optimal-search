#! /usr/env/python
"""
Experiment 1: Examine the impact of changing the number of entities
on the default parameters of the searcher.

The number of entities ranges from a min value to a max value,
chosen randomly.
"""
from src.simulation.environment import Environment
from src.simulation.predator import Predator

import random
from scipy import stats
import numpy as np
import pylab

ENV_SIZE = 1000
N_PATCHES = 20
N_TRIALS = 100
MAX_MOVES = 5000
MAX_ENTITIES_PER_PATCH = 50
MIN_ENTITIES_PER_PATCH = 5
entity_results = []
captured_results = []

for trial in range(N_TRIALS):
    # Set up the environment
    env = Environment(ENV_SIZE, ENV_SIZE, N_PATCHES)
    entities = random.randint(MIN_ENTITIES_PER_PATCH, MAX_ENTITIES_PER_PATCH)
    for patch in env.children:
        patch.create_entities(entities)

    p = Predator()
    p.x_pos = env.length / 2.0
    p.y_pos=env.width / 2.0
    p.parent=env

    for i in range(MAX_MOVES):
        p.move()
        entity = p.detect()
        p.capture(entity)

    entity_results.append(entities)
    captured_results.append(len(p.captured))

# for k in range(len(entity_results)):
#     print(entity_results[k], captured_results[k])

x = np.array(entity_results)
y = np.array(captured_results)

slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
print("Slope, intercept:", slope, intercept)
print("R-squared:", r_value**2)


# Calculate some additional outputs
predict_y = intercept + slope * x
pred_error = y - predict_y
degrees_of_freedom = len(x) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)

# Plotting
pylab.plot(x, y, 'o')
pylab.plot(x, predict_y, 'k-')
pylab.show()
