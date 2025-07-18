#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
eva_str=#
now=0
add=0
mode='now'
operate='flush'

if [ $# -lt 1 ]
then
	echo Usage: sh/eva/run_eva_str.sh eva_str [--day ] 
      	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-mode | --mode)
		shift
		mode=$1
		;;
	-operate | --operate)
		shift
		operate=$1
		;;
	-add | --add_codes | --add)
		shift
		add=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			eva_str=$1
		elif [ $now -eq 1 ]
		then
			operate=$1
		elif [ $now -eq 2 ]
		then
			day=$day
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python engine/eva_str/cli.py run_str $eva_str --day $day --mode $mode --add $add --operate $operate
python engine/eva_str/cli.py run_str $eva_str --day $day --mode $mode --add $add --operate $operate
