#!/bin/bash
# usage sh/buyer/current_branch.sh [day]

day=`date +'%Y-%m-%d'`

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-help | --help)
		echo Usage: sh/buyer/current_branch.sh [day] --day abc [--force xyz]
		exit 2
		;;
	*)
		day=$1
		;;
	esac
	shift
done

echo ls ../stk_daily/$day/juben/|sort
ls ../stk_daily/$day/juben/|sort
