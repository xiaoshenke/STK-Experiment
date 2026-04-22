#!/bin/bash

day=`date +'%Y-%m-%d'`
time_str='0'
mode='now'

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
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo sh/plan/run_template.sh analyze_market_dapiao --day $day
sh/plan/run_template.sh analyze_market_dapiao --day $day

