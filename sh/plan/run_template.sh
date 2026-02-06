#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
template=#
now=0
time_str=#
mode='plan'
ignore_cache=0

if [ $# -lt 1 ]
then
	echo Usage: sh/plan/run_template.sh template [--day ] 
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
	-ignore_cache | --ignore_cache | -ignore | --ignore)
		shift
		ignore_cache=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			template=$1
		elif [ $now -eq 1 ]
		then
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python engine/observe/plan/template_cli.py run_template $template --day $day --mode $mode --time_str $time_str --ignore_cache $ignore_cache
python engine/observe/plan/template_cli.py run_template $template --day $day --mode $mode --time_str $time_str --ignore_cache $ignore_cache

cmd="sh/plan/run_template.sh $template --day $day"
sh/log/log_to_operate.sh "$cmd" "RUN-PLAN-TEMPLATE"
