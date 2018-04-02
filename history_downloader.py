#!/usr/bin/python
import threadpool

# TODO:
def download_func(code,filepath=None):
	print "download_func,code:%s,filepath:%s"%(code,filepath)
	import time
	time.sleep(1)
	return

# codes:[] 
# threaded implementation
def download_history_to_file(codes,filepath,callback=None):
	if not codes or len(codes) == 0:
		return
	pool = threadpool.ThreadPool(10)
	#requests = threadpool.makeRequests(download_func,codes)	
	arg_list = [(code,filepath) for code in codes]
	requests = threadpool.makeRequests(download_func,codes)
	[pool.putRequest(req) for req in requests]
	pool.wait()	
	return 

# FIXME: can't quit from cmd... guess is threadpool
if __name__ == "__main__":
	download_history_to_file(range(100),"abc")
	print "finished"

