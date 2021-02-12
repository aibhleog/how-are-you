'''
This script can be used to plot your feeling tracker data.
To make it more convenient, you can add an alias into your 
.bashrc or .bash_profile file in your home directory that
can look like this:

alias feel="python /path/to/script/see-feelings.py"

Then, you can type feel into your terminal and it will run
the script and pop up the plot for you.
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
feelings = ['bad', 'not the best', 'neutral', "I'm okay", 'good!']

# looking at data
plt.figure(figsize=(8,3.5))
ax = plt.gca() # a quick way to get an axes variable

plt.scatter(df.date,df.feel,s=100,edgecolor='k')
ax.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
ax.minorticks_off()

ax.set_ylim(-0.25,4.25)
ax.set_yticks([0,1,2,3,4,])
ax.set_yticklabels(feelings)

plt.tight_layout()
plt.savefig(path + 'tracker.png')
plt.close()

os.system(f'xdg-open {path}tracker.png')