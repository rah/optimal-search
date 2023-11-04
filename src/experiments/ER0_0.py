#! /usr/env/python
"""
Random search
"""
# %%
import os
import sys
sys.path.append('../../src')

# %%
import util.simutil as su
import analysis.search_dist as sd

#%%
p = su.get_params("./ER0_0.ini")
results = su.runsim(p)

#%%
x, y = sd.extract_search_paths(results)

# %%
sd.plot_search_dist(x, y)
# %%
