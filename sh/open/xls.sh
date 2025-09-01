#!/bin/bash

echo ATTENTION: OPEN-MANUAL-XLS CLI

xls=#
if [ $# -lt 1 ]
then
	echo Usage: sh/open/xls.sh xls [day]
	exit 2
fi

day=#
time_str=#
mode='now'
type='#'
tag=#
codes=#
ignore_cache=1

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
	-mode | --mode)
		shift
		mode=$1
		;;
	-ignore_cache | --ignore_cache)
		shift
		ignore_cache=$1
		;;
	-help | --help)
		echo usage sh/open/pool.sh [--day abc] [--time_str xyz] [--mode aaa ]
		exit 1
		;;
	*)
		xls=$1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/caop/tips/cli.py open_manual_xls $xls --day $day --time_str $time_str --mode $mode --do_log 1
python engine/caop/tips/cli.py open_manual_xls $xls --day $day --time_str $time_str --mode $mode --do_log 1
