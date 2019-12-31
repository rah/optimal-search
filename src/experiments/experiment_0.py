#! /usr/env/python
"""
Run simulation experiments
"""
import src.experiments.runsim as rs

def run_experiment(config=None):
    er, cr = rs.runsim()
    rs.analyse_results(er, cr)

def experiment_0():
    """
    Run experiment with default internal params
    """
    run_experiment()

def experiment_1():
    """
    Run experiment with default external params
    """
    run_experiment("default.ini")
