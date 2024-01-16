#!/bin/bash

export PYTHONUNBUFFERED=1

flush=change

while [ -n "$1" ]
do 
	case "$1" in 
	-flush | --flush)
		shift
		flush=$1
		;;
	*)
		break
		;;
	esac
	shift
done

echo nohup python engine/observe/fengpian/cli.py start_engine_mode --mimic_open 0 --flush $flush 

nohup python engine/observe/fengpian/cli.py start_engine_mode --mimic_open 0 --flush $flush >>observe.fengpian.log 2>&1 &

