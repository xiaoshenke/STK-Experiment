#!/usr/bin/python

import datetime
from log import logger
import calendar

def get_month_start(month,year=2018):
	return '%d-%02d-01'%(year,month)

#def get_month_start(day):
#	day = parse_date_str(day)
#	return '%d-%02d-01'%(day.year,day.month)

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

if __name__ == "__main__":
	print get_month_end('2018-02-03')

