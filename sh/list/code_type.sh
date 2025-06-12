#!/bin/bash

# Usage: sh/list/code_type.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`

if [ $# -eq 1 ]
then
	day=$1
fi

echo python realtime/code_type/reg_cli.py last --day $day
python realtime/code_type/reg_cli.py last --day $day --do_log 1
