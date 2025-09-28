#!/bin/bash

export PYTHONUNBUFFERED=1

type='eva'

day=`date +'%Y-%m-%d'`
now=0

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
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

echo "python engine/observe/buyer/listener_cli.py start_engine_mode $type --day $day  log:observe.buyer.xx_$type.log"
nohup python engine/observe/buyer/listener_cli.py start_engine_mode $type --day $day >>observe.buyer.xx_$type.log 2>&1 &
