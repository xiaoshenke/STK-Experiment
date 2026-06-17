#!/bin/bash

# 计算股票池的pos-high的所有分布

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
time_str='0'
code_type=#
now=0
mode='plan'

if [ $# -lt 1 ]
then
	echo Usage: sh/codes/analyze_pool.sh code-type 
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
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo sh/template/run_xls_template.sh $code_type test_pos_high --day $day --mode $mode --time_str $time_str
sh/template/run_xls_template.sh $code_type test_pos_high --day $day --mode $mode --time_str $time_str


