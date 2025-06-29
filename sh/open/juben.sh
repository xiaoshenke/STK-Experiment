#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
juben=#
do_log=1

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
        -do_log | --do_log)
		shift
		do_log=$1
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

echo python engine/observe/buyer/config_cli.py open_config --day $day --juben $juben --do_log $do_log
python engine/observe/buyer/config_cli.py open_config --day $day --juben $juben --do_log $do_log
