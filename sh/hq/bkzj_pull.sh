#!/bin/bash

day=`date +'%Y-%m-%d'`
time_str='0'
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

echo sh/template/run_template.sh bkzj_pull --day $day --mode $mode --time_str $time_str
sh/template/run_template.sh bkzj_pull --day $day --mode $mode --time_str $time_str

