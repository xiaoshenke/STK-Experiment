#!/bin/bash

echo ATTENTION: wrap realtime/buyer_plan_cli.py 

day=#
time_str=#
mode='now'
type=''
bp_type='default'
ignore_cache=1
debug=0
open=0
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
	-mode | --mode)
                shift
                mode=$1
                ;;
	-debug | --debug)
		shift
		debug=$1
		;;
	-ignore_cache | --ignore_cache)
		shift
		ignore_cache=$1
		;;
	-help | --help)
		echo usage sh/eva_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] type eva [fronts]
		exit 1
		;;
        *)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		elif [ $now -eq 1 ]
		then
			bp_type=$1
		fi
		declare -i now=$now+1
                ;;
        esac
        shift
done

if [[ -z $type ]]
then
	echo type empty.
	exit 2
elif [[ -z $bp_type ]]
then
	echo bp_type empty.
	exit 2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

is_code_type=$(python realtime/buyer_plan_cli.py is_code_type $type)

if [[ $is_code_type == "1" ]]
then

	echo python realtime/buyer_plan_cli.py xls --day $day --time_str $time_str --mode $mode $type $bp_type
	python realtime/buyer_plan_cli.py xls --day $day --time_str $time_str --mode $mode $type $bp_type
else
	echo 当前不支持类型$type $bp_type
fi

