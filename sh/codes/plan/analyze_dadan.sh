#!/bin/bash

if [ $# -lt 1 ]
then
	echo Usage: sh/xls/plan/analyze_dadan.sh [xxx] [day]
	exit 2
fi

xls='bkzj.cdadan:limit=18*find_xls'

day=`date +'%Y-%m-%d'`
time_str='0'
mode='plan'

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

echo sh/template/run_pool_template.sh $xls analyze_dadan --day $day --mode $mode
sh/template/run_pool_template.sh $xls analyze_dadan --day $day --mode $mode

