'''
This script can be used to plot your feeling tracker data,
however this script just shows you overall how you've been 
answering.  This script is currently set up to run at
the end of the "see-feelings.py" script, but it won't
pop up a plot -- it just is meant to update the "hist.png"
figure so you will always have both figures up to date.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
import matplotlib.dates as md
import os

path = '/home/aibhleog/Documents/scratch-code/how-are-you/' # replace with your own path

# reading in file
df = pd.read_csv(path + 'feelings.txt',sep='\t')
feelings = ['bad', 'not the best', 'neutral', 'satisfactory', 'good!']


# looking at a histogram of my responses
plt.figure(figsize=(7,4))
ax = plt.gca() # a quick way to get an axes variable

plt.hist(df.feel,bins=[0,1,2,3,4,5],align='left')

plt.xlim(-0.7,4.7)
plt.ylabel('# of responses')
ax.set_xticks([0,1,2,3,4,])
ax.set_xticklabels(feelings)

plt.text(0.05,0.77,f"Dates: \n{df.loc[0,'date']} to \n{df.loc[len(df)-1,'date']}",\
				transform=ax.transAxes,fontsize=14)

plt.tight_layout()
plt.savefig(path + 'hist.png')
plt.close()

# you can uncomment this if you want -- for now this
# script is run at the end of the "see-feelings.py" script.
#os.system(f'xdg-open {path}hist.png')
