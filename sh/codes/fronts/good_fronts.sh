#!/bin/bash

if [ $# -lt 1 ]
then
	echo Usage: sh/codes/fronts/good_fronts.sh xxx
	exit 2
fi

day=`date +'%Y-%m-%d'`
time_str='0'
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

cmd="sh/codes/fronts/good_fronts.sh $code_type --type $type --day $day --mode $mode --time_str $time_str"
sh/log/log_to_operate.sh "$cmd" "CODES-GOOD-FRONTS"

echo sh/template/run_xls_template.sh $xls good_fronts --day $day --mode $mode --time_str $time_str
sh/template/run_xls_template.sh $xls good_fronts --day $day --mode $mode --time_str $time_str

