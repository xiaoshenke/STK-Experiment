#!/usr/bin/python
import threadpool
import os
from stk_lock import history_file_lock as f_lock
import tushare as ts
import numpy as np

# default download 1 year data 
def download_func(code,filepath=None,start_time=None):
	if not filepath or len(filepath) == 0:
		return
	
	import time
	if not start_time:
		start_time = time_util.get_today_formatted()
	#df = ts.get_h_data(code,start=time_util.get_today_of_last_year_formatted())
	df = ts.get_h_data(code,start=start_time)

	# not forget to add 'code' column
	df['code'] = np.repeat(code,len(df.index))
	if not df or len(df.index) == 0:
		return 
	while not f_lock.acquire():
		pass
	# write file
	try:
		if not os.path.exists(filepath):
			df.to_csv(filepath)
		else:
			import pandas
			origin = pandas.read_csv(filepath)
			df = origin.append(df)
			df.to_csv(filepath)
	except Exception,e:
		pass
	finally:
		f_lock.release()

# codes:[] 
# threaded implementation
def download_history_to_file(codes,filepath,callback=None):
	if not codes or len(codes) == 0:
		return
	pool = threadpool.ThreadPool(10)
	#requests = threadpool.makeRequests(download_func,codes)	
	arg_list = [((code,filepath),{}) for code in codes]
	requests = threadpool.makeRequests(download_func,arg_list)
	[pool.putRequest(req) for req in requests]
	pool.wait()	
	return 

# FIXME: can't quit from cmd... guess is threadpool
# TODO: mac install tushare
if __name__ == "__main__":
	#download_history_to_file(range(100),"abc")
	download_history_to_file(["000789","000023"],"history.csv")
	print "finished"

