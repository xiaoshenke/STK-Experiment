#!/bin/bash

# 打印当前所有的@engine/recorder/ztt/qp_recorder.py 中的数据
# @engine/recorder/ztt/regist/qp_req_cli.py

# Usage: sh/codes/qp/qp_list.sh xx

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH
code_type='0'
day=`date +'%Y-%m-%d'`
time_str='0'
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
	*)
		if [ $now -eq 0 ]
		then
			day=$1
		fi
		;;
	esac
	shift
done


echo python engine/recorder/ztt/regist/qp_req_cli.py last --day $day --time_str $time_str
python engine/recorder/ztt/regist/qp_req_cli.py last --day $day --time_str $time_str
