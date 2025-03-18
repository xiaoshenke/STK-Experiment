#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
yudingyi=#

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		yudingyi=$1
		;;
	esac
	shift
done

echo python engine/observe/buyer/config_cli.py write_yudingyi --day $day $yudingyi
python engine/observe/buyer/config_cli.py write_yudingyi --day $day $yudingyi
