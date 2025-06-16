#!/bin/bash

# 给某个切片加上message

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
type=#
now=0

if [ $# -lt 1 ]
then
	echo Usage: sh/qpc/set_running_list.sh type [--day ]
      	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		elif [ $now -eq 1 ]
		then
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python realtime/qpc_cli.py set_running_list $type --day $day
python realtime/qpc_cli.py set_running_list $type --day $day 
