#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
type='eva'
now=0

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-help | --help)
		echo Usage: sh/buyer/open_config.sh [day] --juben abc
		exit 2
		;;
	*)
		# set value to type|flush_type by now-flag
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

dir=/Users/wuxian/Desktop/stk_daily/$day/buyer/
file=$dir/$type.properties

if [ ! -f "$file" ]
then
	echo 不存在对应的模板文件 先进行模板生成 file:$file
	
	cur_dir=/Users/wuxian/Desktop/STK-Experiment
	file2=$cur_dir/engine/observe/juben/template/buyer.default.properties

	echo cp $file2 $file
	cp $file2 $file
	echo ""
fi

echo open $file
open $file
