#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
message=#
detail=#
type=#
mode='now'
time_str=#
xls=#
now=0

if [ $# -lt 2 ]
then
	echo Usage: sh/message/add_message.sh message type [--day ] [--mode ] [--reason ]
      	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-reason | --reason | -desc | --desc | -detail | --detail)
		shift
		detail=$1
		;;
	-type | --type)
		shift
		type=$1
		;;
	-mode | --mode)
		shift
		mode=$1
		;;
	-time_str | --time_str)
		shift
		time_str=$1
		;;
	-xls | --xls)
		shift
		xls=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			message=$1
		elif [ $now -eq 1 ]
		then
			type=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python realtime/message_cli.py add $message $type --day $day --time_str $time_str --mode $mode --detail $detail --xls $xls
python realtime/message_cli.py add $message $type --day $day --time_str $time_str --mode $mode --detail $detail --xls $xls
