#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
type=#

if [ $# -lt 1 ]
then
	echo Usage: sh/plan/open_template.sh type --day xxx
	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-type | --type)
		shift
		type=$1
		;;
	-help | --help)
		echo Usage: sh/plan/open_templdate.sh [type] --day xxx
		exit 2
		;;
	*)
		type=$1
		;;
	esac
	shift
done

echo python engine/caop/code_type/eva_file/cli.py open_file $type --day $day
python engine/caop/code_type/eva_file/cli.py open_file $type --day $day
