#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
type=#
now=0
time_str=#
mode='now'
operate='flush'
ignore_cache=0

if [ $# -lt 1 ]
then
	echo Usage: sh/tracing/run_codes.sh type [--day ] 
	exit 2
fi

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
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		elif [ $now -eq 1 ]
		then
			operate=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

if [[ $operate == 'info' ]]
then
	echo python engine/observe/tracing/run_cli.py run_codes eva_str0:$type --day $day --mode $mode --time_str $time_str --ignore_cache $ignore_cache
	python engine/observe/tracing/run_cli.py run_codes eva_str0:$type --day $day --mode $mode --time_str $time_str --ignore_cache $ignore_cache
	exit 2
fi

echo python engine/observe/tracing/run_cli.py run_codes eva_str:$type --day $day --mode $mode --time_str $time_str --ignore_cache $ignore_cache
python engine/observe/tracing/run_cli.py run_codes eva_str:$type --day $day --mode $mode --time_str $time_str --ignore_cache $ignore_cache
