#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
type='eva'
now=0

if [ $# -lt 1 ]
then
	echo Usage: sh/buyer/open_file_and_listener.sh xx [--day]
	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-help | --help)
		echo Usage: sh/buyer/open_config.sh [day] --juben abc
		exit 2
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		elif [ $now -eq 1 ]
		then
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo 打开文件: sh/buyer/open_file.sh $type --day $day
sh/buyer/open_file.sh $type --day $day

echo ""

echo 启动监听器: sh/buyer/start_file_listener.sh $type --day $day
sh/buyer/start_file_listener.sh $type --day $day
