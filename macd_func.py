#!/usr/bin/python

import sys
import datetime
from pandas import DataFrame,Series
import pandas as pd
import numpy as np
from functools import partial

from matplotlib import dates as mdates
from matplotlib import ticker as mticker

from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY,YEARLY
from matplotlib.dates import MonthLocator,MONTHLY

import matplotlib.pyplot as plt

# mimic linear function
def linear_func(k,b,x):
	return k*x+b

# mimic parabolic function
def parabolic_func(k,a,b,x):
	return k*(x-a)*(x-a)+b

def movingaverage(values,window):
    weigths = np.repeat(1.0, window)/window
    smas = np.convolve(values, weigths, 'valid')
    return smas

MA1 = 5
MA2 = 10

def create_dataframe(func):
	index = pd.date_range('2017-02-01','2017-04-01',freq='1D')
	df = DataFrame({'kdata':np.arange(1,len(index)+1)},index=index)
	df.kdata = df.kdata.map(func)
	#df.index.name='date'
	df.reset_index(inplace=True)
	df.columns=['date','kdata']
	return df

# TODO
def draw_macd():
	return

# TODO
def draw_func(func):
	df = create_dataframe(func)
	#print df
	Av1 = movingaverage(df.kdata.values,MA1)
	Av2 = movingaverage(df.kdata.values,MA2)
	SP = len(df.kdata.values[MA2-1:])
	
	fig = plt.figure(facecolor='#07000d',figsize=(15,10))
	ax1 = plt.subplot2grid((6,4), (1,0), rowspan=4, colspan=4, axisbg='#07000d')
	ax1.plot(df.date.values[-SP:],df.kdata.values[-SP:],linewidth=1.5,linestyle='--',marker='o')

	Label1 = str(MA1)+' SMA'
	ax1.plot(df.date.values[-SP:],Av1[-SP:],'#e1edf9',label=Label1, linewidth=1.5)

	Label2 = str(MA2)+' SMA'
	ax1.plot(df.date.values[-SP:],Av2[-SP:],'#4ee6fd',label=Label2, linewidth=1.5)

	ax1.grid(True,color='w')
	ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
	ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

	# draw x-axis
	ax1.tick_params(axis='x', colors='w')	
	# draw y-axis
	ax1.tick_params(axis='y', colors='w')   
	plt.show()
	return


def main():
	draw_func(partial(linear_func,0.5,0))
	#draw_func(partial(parabolic_func,-2,5,50))
	return

# Used to explain how macd works 
if __name__ == "__main__":
	main()

