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
		echo Usage: sh/buyer/open_file.sh type [day]
		exit 2
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

buyer_dir=/Users/wuxian/Desktop/stk_daily/$day/buyer/
file=$buyer_dir/$type.properties

if [ ! -f "$file" ]
then
	echo 不存在对应的模板文件 打开失败,可以执行生成tracing文件的流程
	exit 2
fi

echo open $file
open $file


