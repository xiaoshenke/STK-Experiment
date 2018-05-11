#!/usr/bin/python

import datetime

def today_last_year():
    lasty = today() + datetime.timedelta(-365)
    return lasty

def today():
    day = datetime.datetime.today().date()
    return day

if __name__ == "__main__":
	pass
