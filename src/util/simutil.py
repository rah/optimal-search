"""
Simple utilities to run a set of simulation.
"""
import configparser

from simulation.environment import Environment
from simulation.predator import Predator
from random import random

def get_params(config_file="./experiments/default.ini"):
    """Get the parameters for the simulation

    config_file: file name for parameters ini file
    """
    config = configparser.ConfigParser()
    config.read(config_file)

    return config

def runsim(p):
    """Simple wrapper to run a simulation. 
    Parameters for the simulations are contained in a properties file.

    p: configuration parameters
    returns: results
    """
    
    results = {
        'environment': [],
        'predator': []
    }

    for trial in range(p.getint('SIMULATION', 'n_trials')):
        env = Environment(p)

        pred = Predator(p, parent=env)

        # randomise the initial location of the predator
        pred.setx(random() * env.length)
        pred.sety(random() * env.width)

        for i in range(p.getint('SIMULATION', 'max_moves')):
            pred.move()
            entity = pred.detect()
            pred.capture(entity)

        results['environment'].append(env)
        results['predator'].append(pred)

    return results
