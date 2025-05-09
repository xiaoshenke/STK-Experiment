#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
juben=#
force=0

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
	-force | --force)
		shift
		force=$1
		;;
	-help | --help)
		echo Usage: sh/buyer/save_to.sh juben --day abc [--force xyz]
		exit 2
		;;
	*)
		juben=$1
		;;
	esac
	shift
done

echo python engine/observe/buyer/config_cli.py save_to --day $day $juben --force $force
python engine/observe/buyer/config_cli.py save_to --day $day $juben --force $force

echo 
echo 考虑把所有的buyer配置也进行save to?     
echo sh/manual/buyer_cli.sh save_to $juben --day $day --clear 1
