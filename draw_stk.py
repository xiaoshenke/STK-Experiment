#!/usr/bin/python

import sys
from pandas import DataFrame,Series
import pandas as pd
import numpy as np

def read_stk_data(path):
	data = pd.read_csv(path,parse_dates = True,encoding = 'gbk')

	# do a little bit washing job
	data.reset_index()
	data = data.ix[pd.to_datetime(data.date).order().index]
	data.set_index('date',inplace = True)	
	# select only open,high,close,low,volume
	return data[['open','high','close','low','volume']]

def main(path):
	days = read_stk_data(path)
	print days.ix[:10]
	return

# Usage example:python draw_stk.py ts_data.csv
# csv cloumns format:date,open,high,close,low,volume,price_change,p_change,ma5,ma10,ma20,v_ma5,v_ma10,v_ma20,turnover 
if __name__ == "__main__":
	if len(sys.argv) < 1:
		print 'Usage: python draw_stk.py data-path'
		exit()
	main(sys.argv[1])


