#!/bin/bash

echo ATTENTION: OPEN-TIPS CLI

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

xls=#
front=#
day=#
time_str=#
mode='now'
type='buyer'

now=0
while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-time_str | --time_str)
		shift
		time_str=$1
		;;
 	-type | --type)
		shift
		type=$1
		;;
	-mode | --mode)
		shift
		mode=$1
		;;
	-help | --help)
		echo usage sh/tips/eva_cli.sh [--day abc] [--type xyz]
		exit 1
		;;
        *)
		# set value to type|day by now-flag
		if [ $now -eq 0 ]
		then
			xls=$1
		elif [ $now -eq 1 ]
		then
			front=$1
		elif [ $now -eq 2 ]
		then
			type=$1
		fi
		declare -i now=$now+1
                ;;
	esac
	shift
done

echo python engine/caop/tips/cli.py open_front $xls $front --day $day --time_str $time_str --mode $mode --type $type
python engine/caop/tips/cli.py open_front $xls $front --day $day --time_str $time_str --mode $mode --type $type

