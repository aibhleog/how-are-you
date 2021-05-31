'''
This script is meant to provide a way to update your feeling entry
later in the day (if you want to).  I recommend you add this script
as an alias into your terminal, so you can change it from the 
command line.

'''

import numpy as np
import pandas as pd
from datetime import datetime as dt
import os

path = '/home/aibhleog/Documents/scratch-code/how-are-you/' # replace with your own path

# reading in feelings tracker
df = pd.read_csv(path + 'feelings.txt',sep='\t')

print('''
Okay!  We can definitely update your entry for today.
Please input your new feeling update using the ranking below.

===================================================

    How are you feeling, today?  Choose 0-4:

    0 : bad
    1 : not the best
    2 : neutral
    3 : satisfactory
    4 : good!

===================================================
	''')

# prompting for an update for the latest entry -- the present date
feel = input("\nEntry update for today:   ")
try: int(feel)
except: 
	print('Need to input an integer from 0-4.')
	feel = input('Response:  ' )

print() # just for spacing

df.loc[len(df)-1,'feel'] = int(feel)

# saving file
df.to_csv(path + 'feelings.txt',sep='\t',index=False)

os.system("clear") # clears terminal, to make it as if it was never there
