#! /usr/env/python
"""
Run simulation with default parameters
"""
import src.experiments.runsim as rs

er, cr = rs.runsim()
rs.analyse_results(er, cr)
