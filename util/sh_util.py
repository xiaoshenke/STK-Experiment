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
			# TODO: bugfix...
            		break
	        if out != '' and len(out) != 0:
			ret = ret + out
    	return ret


if __name__ == "__main__":
	print exe_shell("echo.sh")

