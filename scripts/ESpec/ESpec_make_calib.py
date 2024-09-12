# define root folder and import LAMP
import sys, os
ROOT_FOLDER = os.path.dirname(__file__) + '/../../' # point this to the folder containing LAMP\
sys.path.append(ROOT_FOLDER)
from LAMP import Experiment
# ----------------------------------
import matplotlib.pyplot as plt 
import numpy as np

# create experiment object 
ex = Experiment(ROOT_FOLDER)

# get ESpec object
ESpec = ex.get_diagnostic('ESpec')

# make calibration file from input
ESpec.make_calib('20241225', save=True, view=True)

# and plot example?
eg_shot = {'date': '20241225', 'run': 'run01', 'burst': 'Burst0001', 'shotnum': 1}
espec_img, x_MeV, y_mrad = ESpec.get_proc_shot(eg_shot)

# -----------------------------------------------------------------------------
plt.show(block=True)
