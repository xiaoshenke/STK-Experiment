#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		day=$1
		;;
	esac
	shift
done

echo python engine/observe/buyer/config_cli.py read_yudingyi --day $day
python engine/observe/buyer/config_cli.py read_yudingyi --day $day 
