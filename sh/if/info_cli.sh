#!/bin/bash

echo ATTENTION: INFO-CMDS CLI

day=#
time_str=#
mode='now'

type=''
tag=#
pool=#
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
	-pool | --pool)
		shift
		pool=$1
		;;
	-ignore_cache | --ignore_cache)
		shift
		ignore_cache=$1
		;;
	-help | --help)
		echo usage sh/info_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] type
		exit 1
		;;
	*)
		type=$1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

	
echo python realtime/caop/code_type.py info $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache --pool $pool
python realtime/caop/code_type.py info $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache --pool $pool

