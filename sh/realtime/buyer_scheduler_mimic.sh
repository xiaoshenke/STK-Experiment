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

echo python realtime/buyer//observe_cli.py set --mimic $mimic
python realtime/buyer//observe_cli.py set --mimic $mimic

