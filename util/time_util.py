#!/usr/bin/python
# coding=utf-8

import datetime
import calendar

# update 2025-08-10: 做一个try catch 
def unix_to_str(t,safe_mode=True):
	import time
	if not safe_mode:
		return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))

	try:
		return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))
	except Exception,e:
		print e
	return '2000-01-01 00:00:00'

def get_month_start(month,year=2018):
	return '%d-%02d-01'%(year,month)

def get_month_end(day):
	day = parse_date_str(day)
	wday,monthRange = calendar.monthrange(day.year, day.month)
	return '%d-%02d-%02d'%(day.year,day.month,monthRange)

# return:date
def parse_date_str(origin):
	return datetime.datetime.strptime(origin,'%Y-%m-%d').date()

def today_last_year():
    lasty = today() + datetime.timedelta(-365)
    return lasty

def today():
    day = datetime.datetime.today().date()
    return day

def next_day(day):
	return str(parse_date_str(day)+datetime.timedelta(1))

def last_day(day):
	return str(parse_date_str(day)+datetime.timedelta(-1))

def get_cur_timestamp(ct=-1):
	import time
	ct = time.time() if ct < 0 else ct
	local_time = time.localtime(ct)
	data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
	data_secs = (ct - long(ct)) * 1000
	time_stamp = "%s.%03d" % (data_head, data_secs)
	return time_stamp

# 获取8位的timestr 
def get_cur_timestr_8():	
	import time
	return unix_to_str(time.time())[-8:]

# util API:
def get_timestr_by_mode(mode):
	if mode == 'open':
		return '09:30:00'
	elif mode == 'noon':
		return '11:30:00'
	elif mode == 'plan':
		return '09:00:00'
	elif mode == 'close':
		return '15:00:00'

	from util.time_util import get_cur_timestr_8
	return get_cur_timestr_8()

if __name__ == "__main__":
	print get_cur_timestamp()
