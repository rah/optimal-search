#! /usr/env/python
"""
Random search
"""

import simutil as su
import analysis.analysis as an

p = su.get_params("./experiments/ER0_1.ini")
results = su.runsim(p)
data = an.extract_data(results)
an.analyse_results(data)