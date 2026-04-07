#!/bin/bash

day=`date +'%Y-%m-%d'`
time_str=#
mode='now'

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
		;;
	esac
	shift
done

# 配置一下analyze pool模式
#echo sh/config/analyze_pool.sh 1
#sh/config/analyze_pool.sh 1

echo sh/template/run_template.sh market_puzhang_analyze --day $day --mode $mode
sh/template/run_template.sh market_puzhang_analyze --day $day --mode $mode


