#!/bin/bash

# Usage: sh/list/code_type.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=$(python util/sh_util.py get_today)

if [ $# -eq 1 ]
then
	day=$1
fi

echo python engine/codes/no_cli.py last --day $day
python engine/codes/no_cli.py last --day $day
