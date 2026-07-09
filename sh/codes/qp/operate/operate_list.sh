#!/bin/bash

# 列出指定切片的所有有效记录

# Usage: sh/codes/qp/operate_list.sh xx

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH
code_type='0'
day=`date +'%Y-%m-%d'`
time_str='0'
now=0

if [ $# -lt 1 ]
then
	echo Usage: sh/codes/qp/operate_list.sh xx
	echo 也可以: python engine/codes/recorder/operate_cli.py last
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
	*)
		if [ $now -eq 0 ]
		then
			code_type=$1
		fi
		;;
	esac
	shift
done


echo python engine/codes/recorder/operate_cli.py qp_hist $code_type --day $day --time_str $time_str
python engine/codes/recorder/operate_cli.py qp_hist $code_type --day $day --time_str $time_str

