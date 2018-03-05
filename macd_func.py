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
EMA = 9

def create_dataframe(func):
	index = pd.date_range('2017-02-01','2017-04-01',freq='1D')
	df = DataFrame({'kdata':np.arange(1,len(index)+1)},index=index)
	df.kdata = df.kdata.map(func)
	df.reset_index(inplace=True)
	df.columns=['date','kdata']
	return df

def draw_func(func):
	df = create_dataframe(func)
	
	Av1 = movingaverage(df.kdata.values,MA1)
	Av2 = movingaverage(df.kdata.values,MA2)
	SP = len(df.kdata.values[MA2-1:])
	
	av1_series = Series(Av1,index=df.index[MA1-1:])
	av1_series.name = 'av1'
	av2_series = Series(Av2,index=df.index[MA2-1:])
	av2_series.name = 'av2'
	df['av1'] = av1_series
	df['av2'] = av2_series
	
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

	df['macd'] = df['av1'] - df['av2']
	Eav = movingaverage(df.macd.values,EMA)
	
	# fixme: why MA2-2?
	eva_series = Series(Eav,index=df.index[MA2-2:])
	df['ema'] = eva_series

	ax2 = plt.subplot2grid((6,4), (5,0), sharex=ax1, rowspan=4, colspan=4, axisbg='#07000d')
	ax2.plot(df.date.values[-SP:], df.macd[-SP:], color='#4ee6fd', lw=2)
	ax2.plot(df.date.values[-SP:], df.ema[-SP:], color='#e1edf9', lw=1)
	ax2.tick_params(axis='x', colors='w')
	ax2.tick_params(axis='y', colors='w')
	plt.show()

	print df
	return


def main():
	#draw_func(partial(linear_func,0.5,0))
	draw_func(partial(parabolic_func,-0.03,40,50))
	return

# Used to explain how macd works 
if __name__ == "__main__":
	main()

