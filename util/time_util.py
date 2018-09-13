#!/usr/bin/python

import datetime
from log import logger

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

