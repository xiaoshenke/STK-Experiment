#!/bin/bash

if [ $# -lt 1 ]
then
	echo Usage: sh/hq/xls_pull_analyze.sh xxx
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

# 配置一下analyze pool模式
#echo sh/config/analyze_pool.sh 0
#sh/config/analyze_pool.sh 0

echo sh/template/run_xls_template.sh $xls pull_analyze --day $day --mode $mode
sh/template/run_xls_template.sh $xls pull_analyze --day $day --mode $mode

