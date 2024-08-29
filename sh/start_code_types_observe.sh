#!/bin/bash

export PYTHONUNBUFFERED=1

# update 2024-01-16: trend->jpg
# update 2024-08-29: jpg->trend
operate=trend
mode="default"
while [ -n "$1" ]
do 
	case "$1" in 
	-operate | --operate)
		shift
		operate=$1
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

echo python engine/observe/code_types/cli.py start_engine_mode --operate $operate --mode $mode
nohup python engine/observe/code_types/cli.py start_engine_mode --operate $operate --mode $mode >>observe.code_types.log 2>&1 &

