#!/bin/bash

day=`date +'%Y-%m-%d'`
message=#
detail=#
type=#
mode='now'
time_str=#
now=0
xls=#

if [ $# -lt 1 ]
then
	echo Usage: sh/message/add_buyer_message.sh message [xls] [--day ] [--mode ] [--reason ]
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
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			message=$1
		elif [ $now -eq 1 ]
		then
			xls=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo sh/message/add_message.sh $message buyer --xls $xls --day $day --time_str $time_str --mode $mode --detail $detail
sh/message/add_message.sh "$message" buyer --xls $xls --day $day --time_str $time_str --mode $mode --detail $detail

