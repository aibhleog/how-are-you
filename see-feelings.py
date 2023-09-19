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

path = '/Users/tahutch1/code/scratch-code/how-are-you/' # replace with your own path

# reading in file
df = pd.read_csv(path + 'feelings.txt',sep='\t')
feelings = ['bad', 'not the best', 'neutral', 'satisfactory', 'good!']

# converting dates to datetime format
dates = [dt.strptime(df.loc[i,'date'],'%d-%b-%Y') for i in df.index.values]


# pre-setting the length of the plot based on # of points
length = len(df)/20
if length > 20: length = 20 # will revisit when we have >1yrs worth of data
if length < 8: length = 8 # for when you're first starting out

# looking at data
plt.figure(figsize=(length,3.5))
ax = plt.gca() # a quick way to get an axes variable

plt.scatter(dates,df.feel,c=df.feel,cmap='BrBG',s=100,edgecolor='k',rasterized=True) # color-coded

# setting up xaxis
interval = int(len(df)/5) # should scale with size of dataframe
ax.xaxis.set_major_formatter(md.DateFormatter('%m/%Y'))
ax.xaxis.set_major_locator(md.DayLocator(interval=interval)) # interval is in days
ax.minorticks_on()

# yaxis
ax.yaxis.set_tick_params(which='minor', left=False, right=False)
ax.set_ylim(-0.25,4.25)
ax.set_yticks([0,1,2,3,4,])
ax.set_yticklabels(feelings)

plt.tight_layout()
plt.savefig(path + 'tracker.png')
plt.close()

# os.system(f'xdg-open {path}tracker.png')
os.system(f'open {path}tracker.png')

# running other plotting script so that both plots are up-to-date the same way
os.system(f'python {path}see-hist.py')
