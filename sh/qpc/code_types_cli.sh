#!/bin/bash

echo ATTENTION: CODE-TYPES-CMDS CLI

day=#
time_str=#
mode=now

type=''
flush_type='trend'
ignore_cache=0

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
	-eva | --eva | --front | -front | --front_type | -front_type)
		shift
		flush_type=$1
		;;
	-ignore_cache | --ignore_cache)
		shift
		ignore_cache=$1
		;;
	-help | --help)
		echo usage sh/cts_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] type
		exit 1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		elif [ $now -eq 1 ]
		then
			flush_type=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

if [ $# -eq 1 ]
then
	type=$1
fi

if [ $# -eq 2 ]
then
	type=$1
	flush_type=$2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

if [[ $flush_type == "trend" ]]
then
	echo python realtime/cts_cli.py trend $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

	python realtime/cts_cli.py trend "$type" --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $flush_type == "flush" ]]
then
	echo python realtime/cts_cli.py flush $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

	python realtime/cts_cli.py flush "$type" --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

else
	echo python realtime/cts_cli.py front $type $flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

	python realtime/cts_cli.py front "$type" $flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache        
fi
