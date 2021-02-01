#!/bin/bash
# usage sh/tail_plan_scheduler.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/plan_scheduler.log
echo tail -f ../stk_daily/$day/plan_scheduler.log
tail -f ../stk_daily/$day/plan_scheduler.log

