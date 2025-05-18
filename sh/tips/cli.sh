#!/bin/bash

echo ATTENTION: OPEN-TIPS CLI

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=#

# 先走一个读取逻辑,设置一下type的值 这个值是前一次打开text文件时记录的
#type=$(python realtime/properties_cli.py read_tips_type)
type=#

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
	-mode | --mode)
		echo 输入了错误的参数: mode
		exit 1
		;;
	-help | --help)
		#echo usage sh/open_tips.sh [--day abc] [--type xyz]
		python engine/caop/tips/cli.py help
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

echo python engine/caop/tips/cli.py open --day $day --type $type
python engine/caop/tips/cli.py open --day $day --type $type

