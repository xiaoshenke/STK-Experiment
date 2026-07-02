#!/bin/bash

path=`pwd`

if [ $# -lt 1 ]
then
	echo Usage: sh/tips/trend/qp_trend.sh codes
	exit 2
fi

day=`date +'%Y-%m-%d'`
now=0
time_str='0'
mode='now'
operate='flush'
ignore_cache=0

codes=$1

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
	-operate | --operate)
		shift
		operate=$1
		;;
	-ignore_cache | --ignore_cache | -ignore | --ignore)
		shift
		ignore_cache=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			codes=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo sh/tips/run_xls_template.sh $codes qp_trend_overall --day $day --mode $mode --time_str $time_str
sh/tips/run_xls_template.sh $codes qp_trend_overall --day $day --mode $mode --time_str $time_str


