'''
This script is just meant to be a cute prompt to check how you're dong every day,
log the answer.  Then, in a separate script, which you can set up an alias for,
you can see a plot of all of your feelings rankings for each day since you started
doing it.

This is meant to be something that could help you track over time how your
overall mental health is doing.

Also, we could easily make this code more complex, but as it's only meant to be 
run once/day, I didn't bother.
'''

import numpy as np
import pandas as pd
from datetime import datetime as dt
import os

# first, the prompt
print('''
===========================================

How are you feeling, today?  Choose 0-4:

0 : bad
1 : not the best
2 : neutral
3 : I'm okay
4 : good!

===========================================
''')

# asking for response
feel = input('Response:  ')
try: int(feel)
except: 
	print('Need to input an integer from 0-4.')
	feel = input('Response:  ' )
	

# logging answer in table
# -----------------------
# first checking file exists (only necessary the first time you run this
if os.path.exists('feelings.txt') == False:
	os.system('touch feelings.txt') # creates file

df = pd.read_csv('feelings.txt',sep='\t',names=['feel','date'])
date = dt.strftime(dt.now(),'%d-%b-%Y')

filler_df = pd.DataFrame({'feel':[feel],'date':[date]})
df = df.append(filler_df,ignore_index=True).copy()

df.to_csv('feelings.txt',sep='\t',index=False)



