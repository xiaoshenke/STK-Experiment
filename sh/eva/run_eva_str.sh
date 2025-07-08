#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
eva_str=#
now=0
add=0
mode='now'

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
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python engine/eva_str/cli.py run_str $eva_str --day $day --mode $mode --add $add
python engine/eva_str/cli.py run_str $eva_str --day $day --mode $mode --add $add
