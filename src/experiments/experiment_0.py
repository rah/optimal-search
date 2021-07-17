#! /usr/env/python
"""
Run simulation experiments
"""
import src.experiments.runsim as rs
import src.analysis.analysis as an

def run_experiment(config_file):
    data = rs.runsim(config_file=config_file)
    an.analyse_results(data)


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
