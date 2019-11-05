#!/usr/bin/python

import datetime
import calendar

def unix_to_str(t):
	import time
	return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))

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

if __name__ == "__main__":
	print get_cur_timestamp()
