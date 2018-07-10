#!/usr/bin/python
# coding=utf-8
from socket import timeout
from threading import Event
exit = Event()
import signal

def quit(signo, _frame):
	print("Interrupted by %d, shutting down" % signo)
	exit.set()

for sig in ('TERM', 'HUP', 'INT'):
	pass
	# exception:signal only works in main thread
	#signal.signal(getattr(signal, 'SIG'+sig), quit);


class WrapperRead:
    def __init__(self,r_obj):
	self.r_obj=r_obj
    
    def read(self):
	return self.r_obj.read()

class Http456Exception(Exception):
    def __init__(self,name="http 456"):
	Exception.__init__(self,name)

class SocketTimeoutException(Exception):
    def __init__(self,name="socket timeout"):
	Exception.__init__(self,name)

def urlopen_till_success(request,timeout):
	try_time = 1
	import time
	sleep_time = 1
	socket_timeout = timeout
	while True:
		try:
			return urlopen(request,socket_timeout)
		except SocketTimeoutException,e:
			print e
			socket_timeout = socket_timeout+1
		except Http456Exception,e:
			print e
			sleep_time = sleep_time+15
			if sleep_time < 60:
				sleep_time = 60
		except Exception,e:
			print e
			pass
		print "urlopen_till_success request:%s try_time:%s sleep:%s"%(request,try_time,sleep_time)
		try_time = try_time+1
		try:
			time.sleep(sleep_time)
		except KeyboardInterrupt:
			print 'receive KeyboardInterrupt'
			break

def urlopen(request,timeout):
	try:
		from urllib.request import urlopen as real_open, HTTPError
	except ImportError:
		from urllib2 import urlopen as real_open, HTTPError
	try:
		ret = real_open(request,timeout=timeout)
		return WrapperRead(ret)
	except HTTPError, e:
		if e.code == 456:
			raise Http456Exception()
		else:
			raise e
	except timeout:
		raise SocketTimeoutException()
	except Exception,e:
		raise e
			


