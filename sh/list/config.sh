#!/bin/bash

# Usage: sh/list/config.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day='#'

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

dir=''

if [[ $day == "#" ]]
then
	dir="realtime/realtime.properties"
else
	dir="../stk_daily/$day/realtime.properties"
fi

echo cat "$dir|grep pool."
echo ""

cat $dir|grep pool.

