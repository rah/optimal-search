"""
Simple utilities to run a set of simulation.
"""
import configparser

def get_params(config_file="/home/rah/workspace/optimal-search/src/experiments/config/default.ini"):
    """
    Get the parameters for the simulation
    config_file: file name for parameters ini file
    """
    config = configparser.ConfigParser()
    config.read(config_file)

    return config