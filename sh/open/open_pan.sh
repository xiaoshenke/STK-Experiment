#!/bin/bash

echo ATTENTION: OPEN-PAN CLI

day=#

# update 2025-03-10: 取消走读取逻辑,因为那样会让行为变的复杂
# 先走一个读取逻辑,设置一下type的值 这个值是前一次打开text文件时记录的
#type=$(python realtime/properties_cli.py read_pan_type)
type='default'

now=0
while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
 	-type | --type)
		shift
		type=$1
		;;
	-help | --help)
		echo usage sh/open_pan.sh [--day abc] [--type xyz]
                exit 1
                ;;
	*)
		# set value to type|day by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		elif [ $now -eq 1 ]
		then
			day=$1
		fi
		declare -i now=$now+1
                ;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/caop/pan/cli.py open --day $day --type $type
python engine/caop/pan/cli.py open --day $day --type $type

