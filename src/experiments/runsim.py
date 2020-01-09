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


def get_params(config_file=None):
    """
    Get the parameters for the simulation
    config_file: file name for parameters ini file
    """
    config = configparser.ConfigParser()
    config.read(config_file)

    return config


def total_entities_in_environment(e):
    n = 0
    for patch in e.children:
        n += patch.number_children()

    return n


def runsim(config_file=None):
    """
    Run the simulation

    config_file: file name of configuration parameters
    """

    entity_results = []
    captured_results = []

    p = get_params(config_file)

    for trial in range(p.getint('SIMULATION', 'n_trials')):
        env = Environment(p)

        pred = Predator(p, parent=env)
        pred.xpos = env.length / 2.0
        pred.y_pos = env.width / 2.0

        for i in range(p.getint('SIMULATION', 'max_moves')):
            pred.move()
            entity = pred.detect()
            pred.capture(entity)

        entity_results.append(total_entities_in_environment(env))
        captured_results.append(pred.total_captured())

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
    pylab.title("Captured vs Total Entities")
    pylab.xlabel("No. Entity in Environment")
    pylab.ylabel("No. Entity Captured")
    pylab.show()
