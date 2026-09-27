#!/bin/bash
# usage sh/ls_noon_report.sh [day]

day=$(python util/sh_util.py get_today)

if [ $# -eq 1 ]
then
	day=$1
fi

ls ../stk_daily/$day/noon_report/
echo ls ../stk_daily/$day/noon_report/

