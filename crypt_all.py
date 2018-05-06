#!/usr/bin/python
import os
import base64

SECRET_FILE = "secret"

ignore_list = ["common.txt","threadpool.py","README.md","crypt_all.py","time_util.py","secret","stk_lock.py","crypt_util.py","crypt_test","hack_urlopen.py","cons.py"]

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
		print "crypt_file,from:%s to:%s"%(file,base64.b64encode(file))
		f = open(file)
		text = f.read()
		text_after = aes.encrypt(text)
		f_write = open(base64.b64encode(file),'w')
		f_write.write(text_after)
		
		print "remove file:%s"%file
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
		print "uncrypt_file,from:%s to:%s"%(file,base64.b64decode(file))
		f = open(file)
		text = f.read()
		text_after = aes.decrypt(text)
		f_write = open(base64.b64decode(file),'w')
		f_write.write(text_after)

		print "remove file:%s"%file
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

# Usage: python crypt_all [-r],if -r is set,will do uncrpyt job
if __name__ == "__main__":
	if True and False:
		from crypt_util import AES_ENCRYPT
		aes = AES_ENCRYPT("secret123")
		uncrypt_file("Y3J5cHRfdGVzdA==",aes)
		import sys
		sys.exit()
	if True and False:
		from crypt_util import AES_ENCRYPT
	        aes = AES_ENCRYPT("secret123")		
		crypt_file("crypt_test",aes)		
		import sys
		sys.exit()
	import sys
	if len(sys.argv) >= 2 and sys.argv[1].lower() == "-r":
		uncrpyt_by_dir()
	else:
		crypt_by_dir()

