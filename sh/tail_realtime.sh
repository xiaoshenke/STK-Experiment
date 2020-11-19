#!/bin/bash
# usage sh/tail_lifecycle.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

echo tail -f ../stk_daily/$day/realtime_plan.log
tail -f ../stk_daily/$day/realtime_plan.log

