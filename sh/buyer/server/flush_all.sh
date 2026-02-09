#!/bin/bash

# Usage: sh/buyer/server/flush_all.sh [time-str]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
time_str=#

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		time_str=$1
		;;
	esac
	shift
done


echo python engine/observe/buyer/server/web_cli.py flush_all --time_str $time_str
python engine/observe/buyer/server/web_cli.py flush_all --time_str $time_str
