#!/bin/bash
# usage sh/ls_fenshi.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=$(python util/sh_util.py get_today)

if [ $# -eq 1 ]
then
        day=$1
fi

file="/Users/wuxian/Desktop/stk_daily/$day//queryable_source//spacing.schedule.csv"

echo head -n 16 $file
head -n 16 $file

echo ""
echo ""
