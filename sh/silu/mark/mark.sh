#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
silu=#
detail='0'
time_str=#
now=0
mode='now'

if [ $# -lt 1 ]
then
	echo Usage: sh/silu/mark/mark.sh silu [detail] 
      	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-reason | --reason | -desc| --desc)
		shift
		detail=$1
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
			silu=$1
		elif [ $now -eq 1 ]
		then
			detail=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python tool/silu/reg_cli.py mark $silu --detail $detail --day $day --time_str $time_str --mode $mode
python tool/silu/reg_cli.py mark $silu --detail $detail --day $day --time_str $time_str --mode $mode

