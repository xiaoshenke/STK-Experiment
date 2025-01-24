#!/bin/bash
# usage sh/realtime/pan_mimic.sh [mimic]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

mimic=1
if [ $# -eq 1 ]
then
	mimic=$1
fi

echo "对pan observe进行mimic操作."

if [ $mimic -eq 1 ]
then
	echo python realtime/observe/pan.py set --running_mode buy
	python realtime/observe/pan.py set --running_mode buy
else
	echo python realtime/observe/pan.py set --running_mode default
	python realtime/observe/pan.py set --running_mode default
fi
