#!/bin/bash

if [ $# -lt 1 ]
then
	echo Usage: sh/bkzj/analyze_bkzj.sh xxx
	exit 2
fi

day=`date +'%Y-%m-%d'`
time_str=#
mode='now'

xls=#

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
		xls=$1
		;;
	esac
	shift
done

echo sh/template/run_pool_template.sh $xls analyze_bkzj --day $day --mode $mode
sh/template/run_pool_template.sh $xls analyze_bkzj --day $day --mode $mode

