#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
type=#
now=0
time_str=#
mode='plan'

if [ $# -lt 1 ]
then
	echo Usage: sh/plan/open_file.sh type [--day ] 
	exit 2
fi

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
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
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

echo python engine/plan2/node/manual_node.py make $type $day
python engine/plan2/node/manual_node.py make $type $day

cmd="sh/plan/open_file.sh $type"
sh/log/log_to_operate.sh "$cmd" "OPEN-PLAN-FILE"
