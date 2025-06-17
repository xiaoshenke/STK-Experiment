#!/bin/bash
# usage sh/ls_bkzj.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
	day=$1
fi

echo "ls ../stk_daily/$day/apply/ | grep bkzj"
ls ../stk_daily/$day/apply | grep bkzj

echo "ls ../stk_daily/$day/apply/ | grep bkzj"
