import time
file_start = time.perf_counter()
# -----------------------------------------------------------------------------
# define root folder and import LAMP
import sys, os
ROOT_FOLDER = os.path.dirname(__file__) + '/../' # point this to the folder containing LAMP and/or the config files
sys.path.append(ROOT_FOLDER)
from LAMP import Experiment
# -----------------------------------------------------------------------------
import matplotlib.pyplot as plt 
import numpy as np

script_start = time.perf_counter()
print(f"Script initialisation time (after loading modules): {(script_start - file_start):0.2f} seconds")

# create experiment object
ex = Experiment(ROOT_FOLDER)

script_start_exp = time.perf_counter()
print(f"Time to create experiment object: {(script_start_exp - script_start):0.2f} seconds")

# get diagnostic
ESpec = ex.get_diagnostic('ESpec')

script_start_diag = time.perf_counter()
print(f"Time to add ESpec diagnostic : {(script_start_diag - script_start_exp):0.2f} seconds")


