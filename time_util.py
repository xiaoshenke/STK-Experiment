#!/usr/bin/python

import datetime

# return:date
def parse_date_str(origin):
	return datetime.datetime.strptime(origin,'%Y-%m-%d').date()

def today_last_year():
    lasty = today() + datetime.timedelta(-365)
    return lasty

def today():
    day = datetime.datetime.today().date()
    return day

