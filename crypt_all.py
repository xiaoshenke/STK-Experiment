#!/usr/bin/python
import os
import base64
from log import logger

SECRET_FILE = "secret"

ignore_list = ["common.txt","threadpool.py","README.md","crypt_all.py","time_util.py","secret","stk_lock.py","crypt_util.py","crypt_test","hack_urlopen.py","cons.py","sh_util.py","log.py","load_memory.py","print_exe_time.py","updater.py"]

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
	if file.endswith(".csv"):
		return False
	if file.endswith(".pyc"):
		return False
	if file in ignore_list:
		return False
	return True

def crypt_file(file,aes):
	if not should_apply_crypt(file):
		return
	if not file.endswith(".py"):
		return
	f = None
	f_write = None
	try:
		f = open(file)
		text = f.read()
		text_after = aes.encrypt(text)
		f_write = open(base64.b64encode(file),'w')
		f_write.write(text_after)
		
                os.remove(file)
	except Exception,e:
		pass
	finally:
		if f:
			f.close()
		if f_write:
			f.close() 
	
def is_base64file(file):
	return file.endswith("==")

def uncrypt_file(file,aes):
	if not should_apply_crypt(file):
		return
	if file.endswith(".py"):
		return
	f = None
	f_write = None
	try:
		f = open(file)
		text = f.read()
		text_after = aes.decrypt(text)
		f_write = open(base64.b64decode(file),'w')
		f_write.write(text_after)

		os.remove(file)
	except Exception,e:
		pass
	finally:
		if f:
			f.close()
		if f_write:
			f.close() 
	
def crypt_by_dir():
	secret = check_and_read_secret()
	if not secret:
		return
	from crypt_util import AES_ENCRYPT
	aes = AES_ENCRYPT(secret)
	for p,dirs,files in os.walk(get_current_dir(),topdown=True):
		for f in files:
			crypt_file(f,aes)
		# only 1 level,so break here
		break

def uncrpyt_by_dir():
	secret = check_and_read_secret()
	if not secret:
		return
	from crypt_util import AES_ENCRYPT
	aes = AES_ENCRYPT(secret)
	
	for p,dirs,files in os.walk(get_current_dir(),topdown=True):
		for f in files:
			uncrypt_file(f,aes)
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

def get_origin_name(crypted_name):
	for p,dirs,files in os.walk(get_current_dir(),topdown=True):
		for f in files:
			if should_apply_crypt(f) and f.endswith(".py"):
				if base64.b64encode(f) == crypted_name:
					return f
		break
	return ""

def get_origin_name_from_list(py_list,crypted_name):
	for f in py_list:
		if base64.b64encode(f) == crypted_name:
			return f
	return ""

def show_helper():
	print "python crypt_all # crypt all .py files of current file"
	print "python crypt_all -r # uncrypt all .py files of current file"
	print "python crypt_all get_origin_name some-crypted-name # get origin name of a crypted file name"
	print "python crypt_all get_origin_name_from_list your-py_list some-crypted-name"
	pass


# Usage: python crypt_all [-r],if -r is set,will do uncrpyt job
if __name__ == "__main__":
	import sys
	if len(sys.argv) < 2:
		crypt_by_dir()
		sys.exit()
	if sys.argv[1].lower() == "-r":
		uncrpyt_by_dir()
		sys.exit()
	if sys.argv[1].lower() == "get_origin_name":
		if len(sys.argv) < 3:
			print "get_origin_name you have to input your crypted-name"
			sys.exit()
		origin = get_origin_name(sys.argv[2])
		print origin
		sys.exit()
	if sys.argv[1].lower() == "get_origin_name_from_list":
		if len(sys.argv) < 4:
			print "get_origin_name_from_list you have to input your py-list and crypted-name"
			sys.exit()
		print get_origin_name_from_list(sys.argv[2].split("\n"),sys.argv[3])
		sys.exit()
	if sys.argv[1] == "-h":
		show_helper()
		sys.exit()
	
