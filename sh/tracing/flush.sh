#!/bin/bash
# usage sh/tracing/trigger.sh [type]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

if [ $# -lt 1 ]
then
	echo Usage: sh/tracing/flush.sh xx
	exit 2
fi

type=$1
echo python realtime/observe/tracing.py trigger  $type
python realtime/observe/tracing.py trigger $type
