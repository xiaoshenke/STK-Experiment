#!/bin/bash
# usage sh/ls_fenshi.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=$(python util/sh_util.py get_today)

if [ $# -eq 1 ]
then
        day=$1
fi

file="/Users/wuxian/Desktop/stk_daily/$day//queryable_source//spacing.reg.csv"

echo cat $file
head -n 11 $file

echo ""

echo python engine/spacing/schedule_cli.py list_all_spacing --day $day
python engine/spacing/schedule_cli.py list_all_spacing --day $day

echo ""


