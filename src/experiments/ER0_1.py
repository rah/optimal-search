#! /usr/env/python
"""
Run simulation experiments
"""
import simutil as su
import src.experiments.runsim as rs
import src.analysis.analysis as an

def run_experiment(config_file):
    data = rs.runsim(config_file=config_file)
    an.analyse_results(data)


def experiment_ER0_1():
    """
    Vary by prey density with low turn rate and low varience
    - Prey density = 10, 20, 40, 80, 160
    - Angle turn = 30
    - Angle varience = low
    """
    # Read default config
    p = su.get_params()

    # Set the patch size to be the same as the environment size
    p['ENVIRONMENT']['min_patches'] = 1
    p['ENVIRONMENT']['max_patches'] = 1
    p['ENVIRONMENT']['max_patch_radius_ratio'] = 1.0

    # Set the number of entities in a patch
    p['PATCH']['max_entities'] = 20
    p['PATCH']['min_entities'] = 20

if __name__ == "__main__":
    # execute only if run as a script
    import sys
    sys.path.append('/home/rah/workspace/optimal-search/src')
    sys.path.append('/home/rah/workspace/optimal-search/src/experiments')
    sys.path.append('/home/rah/workspace/optimal-search/src/simulation')

    experiment_ER0_1()
