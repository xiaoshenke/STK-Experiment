#!/bin/bash

export PYTHONUNBUFFERED=1

only_market=1

while [ -n "$1" ]
do 
	case "$1" in 
	-only_market | --only_market)
		shift
		only_market=$1
		;;
	*)
		break
		;;
	esac
	shift
done

echo nohup python engine/observe/change/cli.py start_engine_mode --mimic_open 0 --only_market $only_market 

nohup python engine/observe/change/cli.py start_engine_mode --mimic_open 0 --only_market $only_market >>observe.change.log 2>&1 &

