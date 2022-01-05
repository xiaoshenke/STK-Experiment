#!/bin/bash
# usage sh/tail_realtime.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

echo less ../stk_daily/$day/realtime_plan.log
less ../stk_daily/$day/realtime_plan.log

