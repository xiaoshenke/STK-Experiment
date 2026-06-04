#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
now=0
time_str=#

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
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			time_str=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python tool/silu/generate_cli.py generate_cmd_list --day $day --time_str $time_str
python tool/silu/generate_cli.py generate_cmd_list --day $day --time_str $time_str

