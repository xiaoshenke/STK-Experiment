#!/usr/bin/python
# coding=utf-8

# 获取xls,type组合的实际路径,
def get_dir_by(day,time_str,xls,type):
	from util.dir_util import get_xls_report_dir
	#type = '%s*%s'%(xls.split('*')[0],type)
	return '%s/%s/%s/%s/'%(get_xls_report_dir(day),time_str.replace(':',''),xls,type)

if __name__ == "__main__":
	pass
