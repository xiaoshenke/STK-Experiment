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
from matplotlib.gridspec import GridSpec


# mimic linear function
def linear_func(k,b,x):
	return k*x+b

# mimic parabolic function
def parabolic_func(k,a,b,x):
	return k*(x-a)*(x-a)+b

def cubic_func(x0,a,b,c,x):
	return a*(x-x0)*(x-x0)*(x-x0) + b*(x-x0) + c

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
	av2_series = Series(Av2,index=df.index[MA2-1:])
	df['av1'] = av1_series
	df['av2'] = av2_series
	
	fig = plt.figure(figsize=(12,8))
	gs = GridSpec(3,3)
	ax1 = plt.subplot(gs[0:-1,:])
	plt.plot(df.date.values[-SP:],df.kdata.values[-SP:],linewidth=1.5,linestyle='--',marker='o')

	Label1 = str(MA1)+' SMA'
	plt.plot(df.date.values[-SP:],Av1[-SP:],'#e1edf9',label=Label1, linewidth=1.5)

	Label2 = str(MA2)+' SMA'
	plt.plot(df.date.values[-SP:],Av2[-SP:],'#4ee6fd',label=Label2, linewidth=1.5)
	plt.ylabel('kdata')
	plt.grid(True)
	ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
	ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

	df['macd'] = df['av1'] - df['av2']
	Eav = movingaverage(df.macd.values,EMA)
	
	# fixme: why MA2-2?
	eva_series = Series(Eav,index=df.index[MA2-2:])
	df['ema'] = eva_series

	ax2 = plt.subplot(gs[-1,:], sharex=ax1)
	plt.plot(df.date.values[-SP:], df.macd[-SP:], color='#4ee6fd', lw=2)
	plt.plot(df.date.values[-SP:], df.ema[-SP:], color='#e1edf9', lw=1)
	plt.ylabel('macd')
	plt.show()

	print df
	return


def main():
	draw_func(partial(cubic_func,30,0.03,-22,10))
	#draw_func(partial(linear_func,0.5,0))
	#draw_func(partial(parabolic_func,-0.03,40,50))
	return

# Used to explain how macd works 
if __name__ == "__main__":
	main()

