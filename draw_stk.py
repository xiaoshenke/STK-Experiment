#!/usr/bin/python

import sys
import datetime
from pandas import DataFrame,Series
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.finance import candlestick
#_ohlc

from matplotlib import dates as mdates
from matplotlib import ticker as mticker

from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY,YEARLY
from matplotlib.dates import MonthLocator,MONTHLY

def format_date(origin):
	return datetime.datetime.strptime(origin,'%Y-%m-%d').date()

import unicodedata
def format_unicode(origin):
	return unicodedata.normalize('NFKD',origin).encode('ascii','ignore')

def movingaverage(values,window):
    weigths = np.repeat(1.0, window)/window
    smas = np.convolve(values, weigths, 'valid')
    return smas

def read_stk_data(path):
	data = pd.read_csv(path,parse_dates = True,encoding = 'gbk')

	# do a little bit washing job
	data.reset_index()
	data = data.ix[pd.to_datetime(data.date).order().index]
	data.set_index('date',inplace = True)	
	# select only open,high,close,low,volume
	return data[['open','high','close','low','volume']]

MA1 = 10
MA2 = 50

def main(path):
	days = read_stk_data(path)

	days_reshape = days.reset_index()
	days_reshape.drop('volume',axis=1,inplace = True)
	days_reshape = days_reshape.reindex(columns=['date','open','high','low','close'])
	import datetime
	days_reshape['date'] = days_reshape['date'].apply(format_unicode)
	days_reshape['date'] = days_reshape['date'].apply(format_date)	
	days_reshape['date'] = mdates.date2num(days_reshape['date'].astype(datetime.date))	
	
	Av1 = movingaverage(days_reshape.close.values, MA1)
	Av2 = movingaverage(days_reshape.close.values, MA2)
	SP = len(days_reshape.date.values[MA2-1:])

	fig = plt.figure(facecolor='#07000d',figsize=(15,10))
	ax1 = plt.subplot2grid((6,4), (1,0), rowspan=4, colspan=4, axisbg='#07000d')
	candlestick(ax1, days_reshape.values[-SP:], width=.6, colorup='#ff1717', colordown='#53c156')

	Label1 = str(MA1)+' SMA'
	Label2 = str(MA2)+' SMA'

	ax1.plot(days_reshape.date.values[-SP:],Av1[-SP:],'#e1edf9',label=Label1, linewidth=1.5)
        ax1.plot(days_reshape.date.values[-SP:],Av2[-SP:],'#4ee6fd',label=Label2, linewidth=1.5)
        ax1.grid(True, color='w')

	ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
	ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	ax1.yaxis.label.set_color("w")
        ax1.spines['bottom'].set_color("#5998ff")
        ax1.spines['top'].set_color("#5998ff")
        ax1.spines['left'].set_color("#5998ff")
        ax1.spines['right'].set_color("#5998ff")
        ax1.tick_params(axis='y', colors='w')
        plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))
        ax1.tick_params(axis='x', colors='w')
        plt.ylabel('Stock price and Volume')
        plt.show()
	
	return

# Usage example:python draw_stk.py ts_data.csv
# csv cloumns format:date,open,high,close,low,volume,price_change,p_change,ma5,ma10,ma20,v_ma5,v_ma10,v_ma20,turnover 
if __name__ == "__main__":
	if len(sys.argv) < 1:
		print 'Usage: python draw_stk.py data-path'
		exit()
	main(sys.argv[1])


