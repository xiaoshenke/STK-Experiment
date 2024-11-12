#!/bin/bash
# usage sh/clear.sh

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

force=0

while [ -n "$1" ]
do 
	case "$1" in 
	-force | --force | --froce)
		shift
		force=$1
		;; 
	*)
		;;
	esac
	shift
done

echo 用于清空配置文件中的所有pool

echo python realtime/pan_config_cli.py clear 
python realtime/pan_config_cli.py clear 

