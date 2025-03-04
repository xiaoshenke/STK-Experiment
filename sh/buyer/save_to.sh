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
		echo Usage: sh/buyer/save_to.sh juben --day abc
		exit 2
		;;
	*)
		juben=$1
		;;
	esac
	shift
done

echo python engine/observe/buyer/config_cli.py save_to --day $day $juben
python engine/observe/buyer/config_cli.py save_to --day $day $juben
