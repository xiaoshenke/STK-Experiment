#!/bin/bash
# usage sh/realtime/buyer_scheduler_mimic.sh [mimic]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

mimic=1
if [ $# -eq 1 ]
then
	mimic=$1
fi

echo "对buyer scheduler进行mimic操作."

if [ $mimic -eq 1 ]
then
	echo python engine/scheduler/buyer/buyer.py set --running_mode buy
	python engine/scheduler/buyer/buyer.py set --running_mode buy
else
	echo python engine/scheduler/buyer/buyer.py set --running_mode default
	python engine/scheduler/buyer/buyer.py set --running_mode default
fi
