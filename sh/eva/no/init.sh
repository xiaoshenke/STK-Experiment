#!/bin/bash

# Usage: sh/list/code_type.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=$(python util/sh_util.py get_today)

if [ $# -eq 1 ]
then
	day=$1
fi

echo python engine/evas/no_cli.py init --day $day
python engine/evas/no_cli.py init --day $day
