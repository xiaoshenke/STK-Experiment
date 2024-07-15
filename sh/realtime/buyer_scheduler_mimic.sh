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

#echo python realtime/buyer//observe_cli.py set --mimic $mimic
#python realtime/buyer//observe_cli.py set --mimic $mimic

if [ $mimic -eq 1 ]
then
	echo python realtime/observe/buyer.py set --running_mode buy
	python realtime/observe/buyer.py set --running_mode buy
else
	echo python realtime/observe/buyer.py set --running_mode default
	python realtime/observe/buyer.py set --running_mode default
fi
