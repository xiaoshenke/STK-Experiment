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

if __name__ == "__main__":
	print exe_shell("echo.sh")

