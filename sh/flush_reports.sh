#!/bin/bash
# usage sh/less_error.sh [day]

day=`date +'%Y-%m-%d'`
time_str=`date +'%H:%M:%S'`
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
		break
		;;
	esac
	shift
done


path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/query_cli.py report_last
python realtime/query_cli.py report_last --day $day --time_str $time_str

