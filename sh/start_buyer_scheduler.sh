#!/bin/bash

export PYTHONUNBUFFERED=1

mimic=0
mode="default"

while [ -n "$1" ]
do 
	case "$1" in 
	-mimic | --mimic)
		shift
		mimic=$1
		;;
	-mode | --mode)
		shift
		mode=$1
		;;
	*)
		break
		;;
	esac
	shift
done

echo python engine/scheduler/buyer/cli.py start_engine_mode --mode $mode --mimic_open $mimic 
nohup python engine/scheduler/buyer/cli.py start_engine_mode --debug 0 --mode $mode --mimic_open $mimic >>scheduler.buyer.log 2>&1 &

