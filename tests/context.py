import os
import sys
import configparser

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../src/simulation')))
import src.simulation.animate
import src.simulation.entity
import src.simulation.environment
import src.simulation.patch
import src.simulation.searcher

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "config.ini"))