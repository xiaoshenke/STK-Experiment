#!/usr/bin/python
# coding=utf-8

# 获取xls,type组合的实际路径,
def get_dir_by(day,time_str,xls,type,fix=0.0):
	from util.dir_util import get_xls_report_dir
	#type = '%s*%s'%(xls.split('*')[0],type)
	if fix > 0:
		return '%s/%s-FIX%s/%s/%s/'%(get_xls_report_dir(day),time_str.replace(':',''),fix,xls,type)

	return '%s/%s/%s/%s/'%(get_xls_report_dir(day),time_str.replace(':',''),xls,type)

# return bool,xls,type,day,time_str
def parse_dir(dir):
	if not dir:
		return False,'','','',''

	# 打一个补丁
	if not dir.endswith('csv'):
		dir = dir+'/'

	# 处理//
	dir = dir.replace('//','/')
	idx = dir.index('xls_report')
	
	day = dir[idx-1-10:idx-1]
	idx2 = dir.find('/',idx+1)
	time_str = dir[idx2+1:idx2+1+6]
	time_str = '%s:%s:%s'%(time_str[0:2],time_str[2:4],time_str[4:6])

	idx3 = dir.find('/',idx2+1)
	idx4 = dir.find('/',idx3+1)
	xls = dir[idx3+1:idx4]

	idx5 = dir.find('/',idx4+1)
	type = dir[idx4+1:idx5]
	return True,xls,type,day,time_str

def demo():
	path = '../stk_daily/2022-04-19/xls_report//090523/xls:core/xls:core*FAST/'
	print parse_dir(path)

import click
@click.group()
def cli():
        """PATH CLI"""
        pass

@cli.command()
@click.argument('path')
def parse(path):
	b,xls,type,day,time_str = parse_dir(path)
	print b
	print xls,type,day,time_str

if __name__ == "__main__":
	#demo()
	cli()
