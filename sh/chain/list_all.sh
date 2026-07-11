#!/bin/bash

# Usage: sh/list/code_type.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
time_str='0'
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
	*)
		if [ $now -eq 0 ]
		then
			day=$1
		elif [ $now -eq 1 ]
                then
			time_str=$1
		fi
		;;
	esac
	shift
done

if [ $# -eq 1 ]
then
	day=$1
fi

echo python engine/recorder/chain/cli.py last --day $day --time_str $time_str
python engine/recorder/chain/cli.py last --day $day --time_str $time_str
