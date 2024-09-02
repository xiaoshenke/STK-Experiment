#!/bin/bash
# usage sh/realtime/buyer_scheduler_mimic.sh [mimic]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

mimic=1
if [ $# -eq 1 ]
then
	mimic=$1
fi

echo "对index observe进行mimic操作."

echo python realtime/observe/index.py set --mimic $mimic
python realtime/observe/index.py set --mimic $mimic


