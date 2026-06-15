#!/bin/bash
# usage sh/realtime/pull_mimic.sh [mimic]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

mimic=1
if [ $# -eq 1 ]
then
	mimic=$1
fi

echo "对pull observe进行mimic操作."

if [ $mimic -eq 1 ]
then
	echo python realtime/observe/pull.py set --running_mode buy
	python realtime/observe/pull.py set --running_mode buy
else
	echo python realtime/observe/pull.py set --running_mode default
	python realtime/observe/pull.py set --running_mode default
fi
