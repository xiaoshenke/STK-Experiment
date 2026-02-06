#!/bin/bash

day=`date +'%Y-%m-%d'`
time_str=#
mode='now'

cmd=''
type=''

# update 2026-01-22: ignore_cache:1->0
ignore_cache=0
debug=0
open=0
now=0

if [ $# -lt 2 ]
then
	echo Usage: sh/log/log_to_operate.sh cmd type
	exit 2
fi

cmd=#
type=#

#if [ $# -eq 2 ]
#then
#	cmd="$1"
#	type="$2"
#fi

while [ -n "$1" ]
do 
	#echo while循环读取到的参数"$1"
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-help | --help)
		echo usage sh/eva_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] type eva [fronts]
		exit 1
		;;
        *)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			cmd="$1"
		elif [ $now -eq 1 ]
		then
			type=$1
		elif [ $now -eq 2 ]
		then
			day=$1
		fi
		declare -i now=$now+1
                ;;
        esac
        shift
done

if [[ -z $type ]]
then
	echo type empty.
	exit 2
elif [[ -z $cmd ]]
then
	echo cmd empty.
	exit 2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

python realtime/operate2.py log "$cmd" $type --day $day

