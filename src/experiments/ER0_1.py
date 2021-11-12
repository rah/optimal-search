#! /usr/env/python
"""
Random search
"""
import src.experiments.simutil as su
import src.experiments.runsim as rs
import src.analysis.analysis as an

p = su.get_params("./src/experiments/config/ER0_1.ini")
results = rs.runsim(p)
data = an.extract_data(results)
an.analyse_results(data)