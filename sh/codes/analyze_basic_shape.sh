#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
time_str='0'
code_type=#
type='0'
now=0
mode='now'

if [ $# -lt 1 ]
then
	echo Usage: sh/codes/analyze_basic_shape.sh code-type 
      	exit 2
fi

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
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			code_type=$1
		elif [ $now -eq 1 ]
		then
			type=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo sh/tips/run_xls_template.sh $code_type analyze_cross_xls_by_basic_shape --day $day --time_str $time_str --mode $mode 
sh/tips/run_xls_template.sh $code_type analyze_cross_xls_by_basic_shape --day $day --time_str $time_str --mode $mode 

