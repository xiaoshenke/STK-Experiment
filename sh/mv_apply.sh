#!/bin/bash
# usage sh/mv_apply.sh --day [day] abc aa:bb:cc dd:ee:ff

day=`date +'%Y-%m-%d'`
while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		break
		;;
	esac
	shift
done

if [ $# -ne 3 ]
then
	echo Usage:sh/mv_apply.sh --day [day] abc aa:bb:cc dd:ee:ff
	exit 2
fi

type=$1
t1=$2
t2=$3

# @ATTENTION: $day\_
echo mv ../stk_daily/$day/apply/$type-$day\_$t1.csv ../stk_daily/$day/apply/$type-$day\_$t2.csv
mv ../stk_daily/$day/apply/$type-$day\_$t1.csv ../stk_daily/$day/apply/$type-$day\_$t2.csv

