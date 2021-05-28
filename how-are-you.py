'''
This script is just meant to be a cute prompt to check how you're dong every day,
log the answer.  Then, in a separate script, which you can set up an alias for,
you can see a plot of all of your feelings rankings for each day since you started
doing it.

This is meant to be something that could help you track over time how your
overall mental health is doing.  Also, we could easily make this code more complex, 
but as it's only meant to be run once/day, I didn't bother.


|------|
| NOTE | 
|------|
| Make sure the entries you use are phrases you don't say a lot, otherwise they may 
| skew your answers.  I used to have 3:"I'm okay" and I had to change it because 
| that's something I say a lot (regardless of how I'm actually doing) and I was 
| choosing that answer when I shouldn't.

'''

import numpy as np
import pandas as pd
from datetime import datetime as dt
import os

path = '/home/aibhleog/Documents/scratch-code/how-are-you/' # replace with your own path

# creating date string for today, will look like ex.: 08-Feb-2021
date = dt.strftime(dt.now(),'%d-%b-%Y')

# boolean varible to mark if already run today
ran = False

# first checking file exists (only necessary the first time you run this)
if os.path.exists(path + 'feelings.txt') == False:
	os.system(f'touch {path}feelings.txt') # creates file
	df = pd.read_csv(path + 'feelings.txt',sep='\t',names=['feel','date']) # specifying columns
else:
	# orginally, the df was read in here, but as it grows in size this could slow down 
	# so I wrote this version instead to just get the tail of the dataset every time for the check
	tail = os.popen(f'tail {path}feelings.txt').read() # writing output to tail
	lastdate = tail.split('\n')[-2].split('\t')[1] # accesses the last date
	
	if lastdate == date: ran = True # don't need to read in feelings.txt
	else: df = pd.read_csv(path + 'feelings.txt',sep='\t') # don't need to specify cols as they now exist

# checking if this has already been run today
# if it has, nothing happens
if ran == False:

	# the prompt
	print('''
===================================================

    How are you feeling, today?  Choose 0-4:

    0 : bad
    1 : not the best
    2 : neutral
    3 : satisfactory
    4 : good!

===================================================
	''')

	# asking for response
	feel = input('Response:  ')
	try: int(feel)
	except: 
		print('Need to input an integer from 0-4.')
		feel = input('Response:  ' )

	print() # just for spacing
		

	# logging answer in table
	# -----------------------

	# appending today's answer to table
	filler_df = pd.DataFrame({'feel':[feel],'date':[date]})
	df = df.append(filler_df,ignore_index=True).copy()

	# saving file
	df.to_csv(path + 'feelings.txt',sep='\t',index=False)

	os.system("clear") # clears terminal, to make it as if it was never there

