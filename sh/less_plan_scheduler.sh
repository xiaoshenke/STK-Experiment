#!/bin/bash
# usage sh/less_plan_scheduler.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/plan_scheduler.log
echo less ../stk_daily/$day/plan_scheduler.log
less ../stk_daily/$day/plan_scheduler.log

