#!/bin/bash
# usage sh/bkzj/get_xls.sh BKxxx

day=#
time_str=#

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-time_str | --time_str)
		shift
		time_str=$1
		;;
	*)
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python util/bkzj_util.py remove $day $time_str
python util/bkzj_util.py remove $day $time_str
