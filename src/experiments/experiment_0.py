#! /usr/env/python
"""
Run simulation experiments
"""
import src.experiments.runsim as rs

def run_experiment(config_file):
    er, cr = rs.runsim(config_file=config_file)
    rs.analyse_results(er, cr)


def experiment_1():
    """
    Run experiment with default external params
    """
    run_experiment("/home/rah/workspace/optimal-search/src/experiments/default.ini")


if __name__ == "__main__":
    # execute only if run as a script
    import sys
    sys.path.append('/home/rah/workspace/optimal-search/src')
    sys.path.append('/home/rah/workspace/optimal-search/src/experiments')
    sys.path.append('/home/rah/workspace/optimal-search/src/simulation')

    experiment_1()
