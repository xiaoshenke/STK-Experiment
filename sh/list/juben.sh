#!/bin/bash

# Usage: sh/list/config.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		day=$1
		;;
	esac
	shift
done

if [ $# -eq 1 ]
then
	day=$1
fi

dir="/Users/wuxian/Desktop/stk_daily/$day/juben/"

echo ls $dir
ls $dir|grep properties

file="/Users/wuxian/Desktop/stk_daily/$day/juben/buyer.config.properties"
if [ -f "$file" ]
then
	echo ""
	echo cat "$dir/buyer*.properties"
	echo cat $file
	cat $file
fi

