#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
type=#
type2='0'
now=0
add=0
mode='now'
operate='flush'
with_logic=-1
time_str=#

if [ $# -lt 1 ]
then
	echo Usage: sh/eva/run_simple_eva.sh "aa->bb" or sh/eva/run_simple_eva.sh aa bb
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
	-time_str | --time_str)
		shift
		time_str=$1
		;;
	-operate | --operate | -op | --op)
		shift
		operate=$1
		;;
	-with_logic | --with_logic | -logic| --logic)
		shift
		with_logic=$1
		;;
	-add | --add_codes | --add)
		shift
		add=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		elif [ $now -eq 1 ]
		then
			type2=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python engine/observe/buyer/runner/code_cli.py run $type --day $day --time_str $time_str --mode $mode --with_logic $with_logic
python engine/observe/buyer/runner/code_cli.py run $type --day $day --time_str $time_str --mode $mode --with_logic $with_logic
