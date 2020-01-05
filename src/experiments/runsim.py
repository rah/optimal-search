#! /usr/env/python
"""
Provides a convenient wrapper to run a set of simulation.
Parameters for the simulations are contained in a properties file.
"""
import configparser
from scipy import stats
import numpy as np
import pylab

from src.simulation.environment import Environment
from src.simulation.predator import Predator


def default_params():
    params = {
        'SIMULATION': {
            'n_trials': 100
        },
        'ENVIRONMENT': {
            'length': 1000,
            'width': 1000,
            'n_patches': 20
        },
        'PATCH': {
            'max_entities_per_patch': 50,
            'min_entities_per_patch': 5
        },
        'SEARCHER': {
            'max_moves': 5000
        }
    }
    return params


def get_params(config_file=None):
    """
    Get the parameters for the simulation
    config_file: file name for parameters ini file
    """

    if config_file is None:
        p = default_params()
    else:
        p = configparser.ConfigParser().read(config_file)

    return p


def total_entities_in_environment(e):
    n = 0
    for patch in e.children:
        n += patch.number_children()

    return n


def create_predator(p, e):
    pred = Predator()
    pred.xpos = e.length / 2.0
    pred.y_pos = e.width / 2.0
    pred.parent = e

    return pred


def run_predator(p):
    p.move()
    entity = p.detect()
    p.capture(entity)


def runsim(config_file=None):
    """
    Run the simulation

    config_file: file name of configuration parameters
    """

    entity_results = []
    captured_results = []

    p = get_params(config_file)

    for trial in range(p['SIMULATION']['n_trials']):
        env = Environment(p)
        pred = create_predator(p, env)

        for i in range(p['max_moves']):
            run_predator(p)

        entity_results.append(total_entities_in_environment(env))
        captured_results.append(pred.total_captured)

    return entity_results, captured_results


def analyse_results(entity_results, captured_results):
    x = np.array(entity_results)
    y = np.array(captured_results)

    slope, intercept, r_value, p_value, \
        slope_std_error = stats.linregress(x, y)

    print("Slope, intercept:", slope, intercept)
    print("R-squared:", r_value**2)

    # Calculate some additional outputs
    predict_y = intercept + slope * x
    pred_error = y - predict_y
    degrees_of_freedom = len(x) - 2
    residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)
    print("Residual Std Error = ", residual_std_error)

    # Plotting
    pylab.plot(x, y, 'o')
    pylab.plot(x, predict_y, 'k-')
    pylab.title("Captured vs Detected Items")
    pylab.xlabel("No. Entity Detected")
    pylab.ylabel("No. Entity Captured")
    pylab.show()
