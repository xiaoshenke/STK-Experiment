#!/bin/bash

# 定位: 快速的找出一些图形形态

if [ $# -lt 1 ]
then
	echo Usage: sh/xls/plan/zhuli_shape.sh xxx [day]
	exit 2
fi

day=`date +'%Y-%m-%d'`
time_str='0'
mode='now'

xls=#
now=0

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-time_str | --time_str)
		shift
		time_str=$1
		;;
	-mode | --mode)
		shift
		mode=$1
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

echo sh/plan/run_xls_template.sh $xls sub_breakma_shape --day $day 
sh/plan/run_xls_template.sh $xls sub_breakma_shape --day $day

