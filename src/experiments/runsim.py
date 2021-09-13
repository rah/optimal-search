#! /usr/env/python
"""
Simple wrapper to run a set of simulation.
Parameters for the simulations are contained in a properties file.
"""
from simutil import get_params

from src.simulation.environment import Environment
from src.simulation.predator import Predator


def runsim(config_file=None):
    """
    Run the simulation

    config_file: file name of configuration parameters
    """

    results = {
        'environment': [],
        'predator': []
    }

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

        results['environment'].append(env)
        results['predator'].append(pred)

    return results
