#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
tips=#

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		tips=$1
		;;
	esac
	shift
done

echo python engine/observe/juben/config_cli.py write_tips --day $day $tips
python engine/observe/juben/config_cli.py write_tips --day $day $tips
