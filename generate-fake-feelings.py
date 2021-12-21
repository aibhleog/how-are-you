'''
This script will generate a fake feelings.txt file to use as an example.
'''

import numpy as np
import pandas as pd
from datetime import datetime as dt
import datetime
import os

path = '/home/aibhleog/Documents/scratch-code/how-are-you/' # replace with your own path


# creating dates
# --------------
base = dt.today()
numdays = 50

start_date = dt.today()-datetime.timedelta(days=numdays) # so that today is the last date
dates = pd.date_range(start_date, periods=numdays).to_pydatetime().tolist()
dates = [dt.strftime(date,'%d-%b-%Y') for date in dates]


# creating feelings (randomly generated)
# -----------------
feel = np.random.randint(0,5,size=numdays)


# final table
final = pd.DataFrame({'feel':feel,'date':dates})
final.to_csv(path + 'random_feelings.txt',sep='\t',index=False)
