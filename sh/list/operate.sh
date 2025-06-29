#!/bin/bash

# Usage: sh/list/code_type.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
size=25

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-size | --size)
		shift
		size=$1
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

dir="/Users/wuxian/Desktop/stk_daily/$day//queryable_source//operate.hist.csv"

echo head -n $size $dir
echo ""

head -n $size $dir

