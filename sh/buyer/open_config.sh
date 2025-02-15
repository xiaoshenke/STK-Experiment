#!/bin/bash
# usage sh/ls_apply.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
	day=$1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/observe/buyer.py open_config_file --day $day
python realtime/observe/buyer.py open_config_file --day $day

