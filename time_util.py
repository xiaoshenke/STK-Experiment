#!/usr/bin/python

import datetime

# return datetime
def get_today_of_last_year():
	now = datetime.datetime.now()
	return datetime.datetime(now.year-1,now.month,now.day,now.hour,now.minute,now.second)

def get_today_of_last_year_formatted():
	day = get_today_of_last_year()
	return day.strftime('%Y-%m-%d')

def get_today_formatted():
	return datetime.datetime.now().strftime('%Y-%m-%d')

if __name__ == "__main__":
	print get_today_of_last_year()

