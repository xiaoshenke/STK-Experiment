#!/bin/bash
# usage sh/clear_pools.sh

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`

force=0

while [ -n "$1" ]
do 
	case "$1" in 
	-force | --force | --froce)
		shift
		force=$1
		;; 
	*)
		day=$1
		;;
	esac
	shift
done

if [ $force -eq 0 ]
then
	echo Usage: sh/config/clear_plan.sh --force 1
	exit 2
fi

echo 将清除plan相关的配置

echo python tool/clear_plan.py clear $day
python tool/clear_plan.py clear $day

