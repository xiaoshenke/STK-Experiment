#!/bin/bash

# Usage: sh/buyer/server/pause_all.sh [pause]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
pause=1

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		pause=$1
		;;
	esac
	shift
done


echo python engine/observe/buyer/server/web_cli.py pause_all $pause
python engine/observe/buyer/server/web_cli.py pause_all $pause
