# define root folder and import LAMP
import sys, os
ROOT_FOLDER = os.path.dirname(__file__) + '/../../' # point this to the folder containing LAMP and/or the config files
sys.path.append(ROOT_FOLDER)
from LAMP import Experiment
# -----------------------------------------------------------------------------
import matplotlib.pyplot as plt 
import numpy as np

# create experiment object
ex = Experiment(ROOT_FOLDER)

# get ESpec diagnostic
ESpec = ex.get_diagnostic('ESpec')

# define a shot
eg_shot = {'date': 20241225, 'run': 'run01', 'shotnum': 1}

# plot
fig, ax = ESpecHigh.plot_proc_shot(eg_shot, debug=True)
#ax.set_xlim([100,2000])
#ax.set_ylim([-50,50])
plt.tight_layout()

# -----------------------------------------------------------------------------
plt.show(block=True)
