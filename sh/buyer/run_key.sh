#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
key=#
type=#
now=0
time_str=#
mode='now'

if [ $# -lt 2 ]
then
	echo Usage: sh/buyer/run_key.sh key type [--day ] 
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
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			key=$1
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

echo python engine/observe/buyer/file_cli.py run_key $key $type --day $day --mode $mode --time_str $time_str
python engine/observe/buyer/file_cli.py run_key $key $type --day $day --mode $mode --time_str $time_str

