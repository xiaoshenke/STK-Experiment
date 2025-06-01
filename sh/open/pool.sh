#!/bin/bash

echo ATTENTION: OPEN-POOL CLI

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
		echo usage sh/open/pool.sh [--day abc] [--time_str xyz] [--mode aaa ] type
		exit 1
		;;
	*)
		day=$1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/manual_cli.py pool $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
python realtime/manual_cli.py pool $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache --do_log 1

