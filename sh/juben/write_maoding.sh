#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
maoding=#

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		maoding=$1
		;;
	esac
	shift
done

echo python engine/observe/juben/config_cli.py write_maoding --day $day $maoding
python engine/observe/juben/config_cli.py write_maoding --day $day $maoding
