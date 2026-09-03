#!/bin/bash

day=`date +'%Y-%m-%d'`
mode='now'
now=0


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
	*)
		# set value to type|flush_type by now-flag
#		if [ $now -eq 0 ]
#		then
#			silu="$1"
#		fi
#		declare -i now=$now+1
		;;
	esac
	shift
done

echo sh/tips/run_template.sh spec_codes_silu_overall --mode $mode --day $day
sh/tips/run_template.sh spec_codes_silu_overall --mode $mode --day $day
