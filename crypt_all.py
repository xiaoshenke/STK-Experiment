#!/usr/bin/python
import os
import base64

SECRET_FILE = "secret"

ignore_list = ["common.txt","threadpool.py","README.md","crypt_all.py","time_util.py","secret","stk_lock.py","crypt_util.py"]

def get_current_dir():
	import sys,os
	path = sys.path[0]
	if os.path.isdir(path):
		return path
	return os.path.dirname(path)

def should_apply_crypt(file):
	if not file or len(file) == 0:
		return False
	if file.startswith("."):
		return False
	if file.endswith(".sh"):
		return False
	if file in ignore_list:
		return False
	return True

# TODO: crpyt and write file
def crypt_file(file):
	if not should_apply_crypt(file):
		return
	print "crypt_file,from:%s to:%s"%(file,base64.b64encode(file))
	
def is_base64file(file):
	return file.endswith("==")

# TODO: uncrpyt and write file
def uncrypt_file(file):
	if not should_apply_crypt(file):
		return
	if not is_base64file(file):
		return
	try:
		print "uncrypt_file,from:%s to:%s"%(file,base64.b64decode(file))
	except Exception,e:
		pass

def crypt_by_dir():
	secret = check_and_read_secret()
	if not secret:
		return
	for p,dirs,files in os.walk(get_current_dir(),topdown=True):
		for f in files:
			crypt_file(f)
		# only 1 level,so break here
		break

def uncrpyt_by_dir():
	secret = check_and_read_secret()
	if not secret:
		return
	for p,dirs,files in os.walk(get_current_dir(),topdown=True):
		for f in files:
			uncrypt_file(f)
		# only 1 level,so break here
		break

# return None if no secret
def check_and_read_secret():
	if not os.path.exists(SECRET_FILE):
		return None
	f = open(SECRET_FILE,'r')
	try:
		sec = f.read()
		return sec
	except Exception,e:
		return None
	finally:
		f.close()

# Usage: python crypt_all [-r],if -r is set,will do uncrpyt job
if __name__ == "__main__":
	import sys
	if len(sys.argv) >= 2 and sys.argv[1].lower() == "-r":
		uncrpyt_by_dir()
	else:
		crypt_by_dir()

