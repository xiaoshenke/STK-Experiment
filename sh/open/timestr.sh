#!/bin/bash
# usage sh/open/timestr.sh ABC

if [ $# -lt 1 ]
then
	echo usage sh/open/timestr.sh ABC
	exit 2
fi

time_str=#
day=#

now=0
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
	-help | --help)
		echo usage sh/open/timestr.sh time_str [--day abc] 
		exit 1
		;;
	*)
		time_str=$1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/opener/manual_cli.py open_timestr $time_str --day $day
python engine/opener/manual_cli.py open_timestr $time_str --day $day

