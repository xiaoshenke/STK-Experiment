#!/bin/bash

# Usage: sh/buyer/log/list_all.sh [day]

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

echo ""
echo "按照纪录到数据的时间戳 而不是计算时间戳进行逆序排序"

echo python engine/observe/buyer/request/log_cli.py success_codes_list --day $day
python engine/observe/buyer/request/log_cli.py success_codes_list --day $day
