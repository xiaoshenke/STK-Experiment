#!/bin/bash

echo ATTENTION: OPEN-TIPS CLI

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

xls=#
day=#
type='buyer'

now=0
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
	-mode | --mode)
		echo 输入了错误的参数: mode
		exit 1
		;;
	-help | --help)
		echo usage sh/xls_tips.sh [--day abc] [--type xyz]
		exit 1
		;;
        *)
		# set value to type|day by now-flag
		if [ $now -eq 0 ]
		then
			xls=$1
		elif [ $now -eq 1 ]
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

echo python engine/caop/tips/cli.py open_xls $xls --day $day --type $type
python engine/caop/tips/cli.py open_xls $xls --day $day --type $type

