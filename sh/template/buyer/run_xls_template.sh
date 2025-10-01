#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
xls=#
template='buyer'
now=0
time_str=#
mode='now'
operate='flush'
ignore_cache=0

if [ $# -lt 1 ]
then
	echo Usage: sh/buyer/run_xls_template.sh xls template [--day ] 
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
	-operate | --operate | -operater | --operater)
		shift
		operate=$1
		;;
	-ignore_cache | --ignore_cache)
		shift
		ignore_cache=$1
		;;
	-help | --help)
		echo Usage: sh/buyer/run_xls_template.sh xls template [--day ]
		echo ""
		head -n 15 engine/caop/buyers/template/run_xls_template.py
		exit 2
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

echo python engine/caop/buyers/template/cli.py run_xls_template $xls $template --day $day --mode $mode --time_str $time_str --ignore_cache $ignore_cache --operate $operate
python engine/caop/buyers/template/cli.py run_xls_template $xls $template --day $day --mode $mode --time_str $time_str --ignore_cache $ignore_cache --operate $operate

