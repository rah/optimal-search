#! /usr/env/python
"""
Provides a convenient wrapper to run a set of simulation.
Parameters for the simulations are contained in a properties file.
"""
from environment import Environment
from searcher import Searcher

import random
from scipy import stats
import numpy as np
import pylab

entity_results = []
captured_results = []


def default_params():
    params = {
        'env_size': 1000,
        'n_patches': 20,
        'n_trials': 100,
        'max_moves': 5000,
        'max_entities_per_patch': 50,
        'min_entities_per_patch': 5,
    }
    return params


def config_params(config_file):
    return {}


def runsim(config_file=None):
    p = {}

    # get the paramters for the simulation
    if config_file is None:
        p = default_params()
    else:
        p = config_params(config_file)

    for trail in range(p['n_trials']):
        # Set up the environment
        env = Environment(p['env_size'], p['env_size'], p['n_patches'])
        entities = random.randint(p['min_entities_per_patch'],
                                  p['max_entities_per_patch'])
        for patch in env.children:
            patch.create_entities(entities)

        s = Searcher(x_pos=(env.length / 2.0),
                     y_pos=(env.width / 2.0),
                     parent=env)

        for i in range(p['max_moves']):
            s.move()
            entity = s.detect()
            s.capture(entity)

        entity_results.append(entities)
        captured_results.append(len(s.captured))

        # for k in range(len(entity_results)):
        #     print(entity_results[k], captured_results[k])

    x = np.array(entity_results)
    y = np.array(captured_results)

    slope, intercept, r_value, p_value, \
        slope_std_error = stats.linregress(x, y)

    print "Slope, intercept:", slope, intercept
    print "R-squared:", r_value**2

    # Calculate some additional outputs
    predict_y = intercept + slope * x
    pred_error = y - predict_y
    degrees_of_freedom = len(x) - 2
    residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)
    print "Residual Std Error = ", residual_std_error

    # Plotting
    pylab.plot(x, y, 'o')
    pylab.plot(x, predict_y, 'k-')
    pylab.show()





