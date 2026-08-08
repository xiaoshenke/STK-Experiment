#!/bin/bash
# usage sh/ls_report.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=$(python util/sh_util.py get_today)

if [ $# -eq 1 ]
then
	day=$1
fi

ls ../stk_daily/$day/report/
echo ls ../stk_daily/$day/report/

