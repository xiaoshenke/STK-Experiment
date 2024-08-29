#!/bin/bash

export PYTHONUNBUFFERED=1

# update 2024-01-16: trend->jpg
# update 2024-08-29: jpg->trend
operate=trend

while [ -n "$1" ]
do 
	case "$1" in 
	-operate | --operate)
		shift
		operate=$1
		;;
	*)
		break
		;;
	esac
	shift
done

echo python engine/observe/code_types/cli.py start_engine_mode --operate $operate
nohup python engine/observe/code_types/cli.py start_engine_mode --operate $operate >>observe.code_types.log 2>&1 &

