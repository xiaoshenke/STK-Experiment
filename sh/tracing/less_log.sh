#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
now=0
xls='0'

if [ $# -lt 1 ]
then
	echo Usage: sh/tracing/tail_log.sh xls [type] [to-name] [--day]
	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		if [ $now -eq 0 ]
		then
			xls=$1
		elif [ $now -eq 1 ]
		then
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

log_file="/Users/wuxian/Desktop/stk_daily/$day/observe.tracing.xx_$xls.log"

if [ ! -f "$log_file" ]
then
	echo 不存在对应的日志文件 $log_file
	ls /Users/wuxian/Desktop/stk_daily/$day/|grep observe|grep xx_|grep log
	exit 2
fi

echo less $log_file
less $log_file

