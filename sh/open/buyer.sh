#!/bin/bash

echo ATTENTION: OPEN-BUYER CLI

day=#

now=0
while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-help | --help)
		echo usage sh/open/buyer.sh [--day abc] 
		exit 1
		;;
	*)
		day=$1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/caop/tips/cli.py open_manual_buyer --day $day
python engine/caop/tips/cli.py open_manual_buyer --day $day --do_log 1

