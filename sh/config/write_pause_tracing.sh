#!/bin/bash

# 暂停tracing标志位

if [ $# -ne 1 ]
then
	echo usage sh/config/write_pause_tracing.sh val
	exit 1
fi

val=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/properties_cli.py write_pause_tracing $val 
python realtime/properties_cli.py write_pause_tracing $val

