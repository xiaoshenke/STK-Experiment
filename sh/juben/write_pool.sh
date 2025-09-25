#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
pool=#

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		pool=$1
		;;
	esac
	shift
done

echo python engine/observe/juben/config_cli.py write_pool --day $day $pool
python engine/observe/juben/config_cli.py write_pool --day $day $pool
