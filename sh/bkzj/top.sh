#!/bin/bash

echo ATTENTION: MANUAL-CMDS CLI

day=#
time_str=#
mode='now'

type='bkzj.top'
tag=#
codes=#
ignore_cache=1
debug=0
version=0

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
	-debug | --debug)
		shift
		debug=$1
		;;
	-tag | --tag)
		shift
		tag=$1
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
		echo usage sh/realtime/flush_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] type
		exit 1
		;;
	*)
		version=$1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo sh/bkzj/use_api.sh $version
sh/bkzj/use_api.sh $version

echo python realtime/observe/pan.py do_manual $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache --debug $debug
        
python realtime/observe/pan.py do_manual $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache --debug $debug

