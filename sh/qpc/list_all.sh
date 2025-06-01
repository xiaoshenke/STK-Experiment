#!/bin/bash

# Usage: sh/list/code_type.sh [day]

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

if [ $# -eq 1 ]
then
	day=$1
fi

echo python realtime/qpc_cli.py last --day $day
python realtime/qpc_cli.py last --day $day
