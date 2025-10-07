#!/bin/bash

# 运行指定文件(默认为eva)的买点文件

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
file='eva'
now=0
time_str=#
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
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			file=$1
		elif [ $now -eq 1 ]
		then
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python engine/observe/buyer/file_cli.py run_file $file --day $day --mode $mode --time_str $time_str
python engine/observe/buyer/file_cli.py run_file $file --day $day --mode $mode --time_str $time_str


