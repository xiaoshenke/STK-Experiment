#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
juben=#

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-juben | --juben)
		shift
		juben=$1
		;;
	-help | --help)
		echo Usage: sh/buyer/open_config.sh [day] --juben abc
		exit 2
		;;
	*)
		day=$1
		;;
	esac
	shift
done

python engine/observe/eva/file_cli.py open_config --day $day
python engine/observe/eva/file_cli.py open_config --day $day --do_log 1
