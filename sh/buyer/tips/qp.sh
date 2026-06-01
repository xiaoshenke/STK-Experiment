#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
xls=#
template='none'
now=0
time_str=#
mode='plan'
operate='flush'
with_logic=-1
ignore_cache=0

if [ $# -lt 1 ]
then
	echo Usage: sh/tips/run_qp_template.sh xls template [--day ] 
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
	-operate| --operate)
		shift
		operate=$1
		;;
        -with_logic | --with_logic | -logic| --logic)
		shift
		with_logic=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			xls=$1
		elif [ $now -eq 1 ]
		then
			template=$1
		elif [ $now -eq 2 ]
		then
			operate=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done


echo python engine/observe/buyer/tips_cli.py run_qp_template $xls $template --day $day --mode $mode --time_str $time_str --operate $operate --ignore_cache $ignore_cache
python engine/observe/buyer/tips_cli.py run_qp_template $xls $template --day $day --mode $mode --time_str $time_str --operate $operate --ignore_cache $ignore_cache
