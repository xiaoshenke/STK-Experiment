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
	*)
		day=$1
		;;
	esac
	shift
done

echo python engine/observe/buyer/config_cli.py open_config --day $day --juben $juben
python engine/observe/buyer/config_cli.py open_config --day $day --juben $juben
