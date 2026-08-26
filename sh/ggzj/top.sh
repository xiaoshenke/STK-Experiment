#!/bin/bash
# usage sh/ggzj/top.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=$(python util/sh_util.py get_today)

if [ $# -eq 1 ]
then
	day=$1
fi

echo python engine/xls/cli.py apply_and_save ggzj $day
python engine/xls/cli.py apply_and_save ggzj $day
