#!/bin/bash

# Usage: sh/list/subs.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day='#'
#`date +'%Y-%m-%d'`

if [ $# -eq 1 ]
then
	day=$1
fi

echo python realtime/properties_cli.py list_subs_key --day $day
python realtime/properties_cli.py list_subs_key --day $day
