#!/usr/bin/python
# coding=utf-8

import os
import sys
import base64
from log import logger

IS_WINDOWS = False
DEBUG_OPEN = False
SECRET_FILE = "secret"

ignore_list = [ "common.txt","threadpool.py","README.md","crypt_all.py","crypt_cli.py","time_util.py","secret","stk_lock.py","crypt_util.py","crypt_test","hack_urlopen.py","cons.py","sh_util.py","log.py","load_memory.py","print_exe_time.py","updater.py","__init__.py","dir_util.py","crontab.py",".DS_Store","realtime.properties",".gitignore" ]

ignore_dirs = ["/.git","/csv_data","/other","/data"]

def get_base_dir():
	# 要求必须在工程下执行
	dir = os.getcwd()
	s = 'STK-Experiment'
	idx = dir.index(s)
	return dir[:idx+len(s)]

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
		pass
	if file.endswith(".sh"):
		return False
	if file.endswith(".csv"):
		return False
	if file.endswith(".pyc"):
		return False
	if file.endswith('.out'):
		return False
	if file.endswith('.log'):
		return False
	if file in ignore_list:
		return False

	return True

def crypt_file(file,aes,base_dir=None,debug=False):
	if not should_apply_crypt(file):
		return
	if not file.endswith(".py"):
		return

	if not aes:
		from crypt_util import AES_ENCRYPT
		secret = check_and_read_secret()
		aes = AES_ENCRYPT(secret)

	if debug:
		print u'crypt_all.crypt_file,file:%s'%(file)

	f = None
        f_write = None
        seperator = '/' if not IS_WINDOWS else '\\'
        try:
		from_file = file if not base_dir else base_dir + seperator + file
		#print from_file

		f = open(from_file)
		text = f.read()
		text_after = aes.encrypt(text)

		to_file = base64.b64encode(file) if not base_dir else base_dir + seperator + base64.b64encode(file)

                if DEBUG_OPEN:
                        logger.debug("from file:%s, to file:%s",from_file,to_file)

		if debug:
			print 'from file:%s, to file:%s'%(from_file,to_file)
		f_write = open(to_file,'w')
                f_write.write(text_after)
                if f:
                    f.close()
                    f = None
                os.remove(from_file)
        except Exception,e:
		logger.debug(e)
		pass
	finally:
		if f:
			f.close()
		if f_write:
			f_write.close() 
	
def is_base64file(file):
	return file.endswith("==")

def uncrypt_file(file,aes,base_dir=None,debug=False):
	if debug:
		print u'util.crypt_all.uncrypt_file,file:%s'%(file)
	if not should_apply_crypt(file):
		if debug:
			print u'should_apply_crypt return false.'
		return
	if file.endswith(".py"):
		return

	if not aes:
		from crypt_util import AES_ENCRYPT
		secret = check_and_read_secret()
		aes = AES_ENCRYPT(secret)

	f = None
	f_write = None
	from_file = file if not base_dir else base_dir + "/" + file

	try:

		f = open(from_file)
		text = f.read()
		text_after = aes.decrypt(text)

		to_file = base64.b64decode(file) if not base_dir else base_dir + "/" + base64.b64decode(file)
                if DEBUG_OPEN:
                        logger.debug("from file:%s,to file:%s",from_file,to_file)

		if debug:
			print 'from file:%s,to file:%s'%(from_file,to_file)

		f_write = open(to_file,'w')
		f_write.write(text_after)
                if f:
                        f.close()
                        f = None
		os.remove(from_file)
	except Exception,e:
		print e,from_file
		pass
	finally:
		if f:
			f.close()
		if f_write:
			f_write.close() 
	
def crypt_by_dir():
	secret = check_and_read_secret()
	if not secret:
		return

	from crypt_util import AES_ENCRYPT
	aes = AES_ENCRYPT(secret)
	dir = get_base_dir()
	for p,dirs,files in os.walk(dir,topdown=True):
		ignore = False
		for ig in ignore_dirs:
			if ig in p:
				ignore = True
				break
		if ignore:
			continue
                if DEBUG_OPEN:
                        logger.debug("in crypt_by_dir,p:%s",p)
		for f in files:
                        if DEBUG_OPEN:
                               logger.debug("we will crypt file:%s",f)
			crypt_file(f,aes,p)
	return	

def uncrpyt_by_dir():
	secret = check_and_read_secret()
	if not secret:
		return
	from crypt_util import AES_ENCRYPT
	aes = AES_ENCRYPT(secret)
	dir = get_base_dir()
	for p,dirs,files in os.walk(dir,topdown=True):
		ignore = False
		for ig in ignore_dirs:
			if ig in p:
				ignore = True
				break
		if ignore:
			continue
	
		for f in files:
			uncrypt_file(f,aes,p)
	return

# return None if no secret
def check_and_read_secret():
	from cons import CUR_PATH
	file = "%s/%s"%(CUR_PATH,SECRET_FILE)

	if DEBUG_OPEN:
		logger.debug("crypt_all.check_and_read_secret try read file:%s",file)

	if not os.path.exists(file):
		return None
	f = open(file,'r')
	try:
		sec = f.read()
                if DEBUG_OPEN:
                      logger.debug("read secret:%s",sec)
		return sec
	except Exception,e:
		return None
	finally:
		f.close()

def get_origin_name(crypted_name):
	if DEBUG_OPEN:
		logger.debug("crpyt_all.get_origin_name,crypted_name:%s",crypted_name)
	dir = get_base_dir()
	for p,dirs,files in os.walk(dir,topdown=True):
		for f in files:
			if should_apply_crypt(f) and f.endswith(".py"):
				if base64.b64encode(f) == crypted_name:
					return f
		break
	return ""

def get_origin_name_from_list(py_list,crypted_name):
	if DEBUG_OPEN:
		logger.debug("crypt_all.get_origin_name_from_list py_list:%s",py_list)

	#print 'get_origin_name_from_list,len-py-list:%s %s'%(len(py_list),crypted_name)

	# 当前文件夹
	if not '/' in crypted_name:
		for f in py_list:
			if base64.b64encode(f) == crypted_name:
				return f
		return ""

	# 子目录
	idx = crypted_name.rfind('/')
	a = crypted_name[:idx]
	b = crypted_name[idx+1:]
	for f in py_list:
		if not '/' in f:
			continue
		idx = f.rfind('/')
		fa = f[:idx]
		fb = f[idx+1:]
		if fa != a:
			continue
		if base64.b64encode(fb) == b:
			return f
	return ""

def show_helper():
	print "python crypt_all # crypt all .py files of current file"
	print "python crypt_all -r # uncrypt all .py files of current file"
	print "python crypt_all get_origin_name some-crypted-name # get origin name of a crypted file name"
	print "python crypt_all get_origin_name_from_list your-py_list some-crypted-name"
	return

def deal_cmd():
	import sys
	if len(sys.argv) < 2:
		crypt_by_dir()
		return

	if sys.argv[1].lower() == "-r":
		uncrpyt_by_dir()
		return

	if sys.argv[1].lower() == "get_origin_name":
		if len(sys.argv) < 3:
			print "get_origin_name you have to input your crypted-file-name"
			sys.exit()

		#print u'util.crypt_all.deal_cmd,get_origin_name:%s'%sys.argv[2]
		origin = get_origin_name(sys.argv[2])
		print origin
		return

	if sys.argv[1].lower() == "get_origin_name_from_list":
		if len(sys.argv) < 4:
			print "get_origin_name_from_list you have to input your py-list and crypted-name"
			return
		print get_origin_name_from_list(sys.argv[2].split("\n"),sys.argv[3])
		return

	if sys.argv[1] == "-h":
		show_helper()
		return
	return
	
# Usage: python crypt_all [-r],if -r is set,will do uncrpyt job
if __name__ == "__main__":
	import sys
	deal_cmd()
