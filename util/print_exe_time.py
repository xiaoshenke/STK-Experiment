#!/usr/bin/python
# coding=utf-8
import time
from log import logger
from util.mini import to_float2

def print_exe_time():
	def _print_exe_time(func):
		def _real(*args,**kwargs):
			start = time.time()
			ret = func(*args,**kwargs)
			if "at 0x" in str(func):
				idx = str(func).index("at 0x")			
				print "method:%s runs %s seconds!"%(str(func)[:idx-1]+">",to_float2(time.time()-start))
			else:
				print "method:%s runs %s seconds!"%to_float2(func,time.time()-start)
			return ret
		return _real
	return _print_exe_time

def a_func():
	def _a():
		return 1
	print_exe_time()(_a)()

def b_func():
	print_exe_time()(time.sleep)(2)

if __name__ == "__main__":
	a_func()

