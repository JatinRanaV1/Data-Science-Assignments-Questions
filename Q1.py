import numpy as np
import pandas as pd
from numpy.random import randint
import time

t={}
for i in range(1,6):
	size=i*5000
	values=randint(0,5000,size)
	start=time.time()
	values.sort()
	t[size]=(time.time()-start)

dataset=pd.DataFrame(t.items(),columns=['Number of elements in a list','Time Taken to sort (in sec)'])
dataset.to_csv('Q1.csv')
