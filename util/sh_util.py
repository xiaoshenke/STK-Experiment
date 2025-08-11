#!/usr/bin/python
# coding=utf-8
import os
import subprocess

def exe_shell(shell_name,pm_list=[]):
	cpath = os.path.abspath('.')
	t = []
	t.append(cpath+'/'+shell_name)

	# Fixed a bug here
	t.insert(0,'/bin/bash')
	t.extend(pm_list)
	return subprocess.call(t)

from subprocess import *

# wrapper sh code,return stdout string
def sh_wrapper_string(args,out=PIPE):
	if not args or len(args) == 0:
		return ""
	
	ret = ""
	process = Popen(args, stdout=out, stderr=STDOUT,universal_newlines=True)
	while True:
		if process.stdout == None:
			break
        	out = process.stdout.read(1)
        	if out == '' and process.poll() != None:
            		break
	        if out != '' and len(out) != 0:
			ret = ret + out
    	return ret

# util API:
def call_shell_and_return_msgs(cmd):
	print u'\n>>>>>>>>>>>>>>>>>>>>>>> running shell command: %s,wait...........\n'%(cmd)

	import time
	start = time.time()

	import os
	sub = os.popen( cmd )
	ret = sub.readlines()

	from util.mini import to_float2
	cost = time.time()-start
	cost = to_float2(cost)
	msg = u'\n调用shell结束 花费:%s 秒\n'%(cost)
	print msg

	return ret

if __name__ == "__main__":
	pass
