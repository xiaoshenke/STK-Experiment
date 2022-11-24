#!/bin/bash
# usage sh/reporter_mimic.sh [mimic]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

mimic=1
if [ $# -eq 1 ]
then
	mimic=$1
fi

echo "对plan reporter server进行mimic操作."

echo python realtime/report_cli.py set --mimic $mimic
python realtime/report_cli.py set --mimic $mimic

