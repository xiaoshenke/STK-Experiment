#!/bin/bash
# usage sh/less_ban24.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

echo less ../stk_daily/$day/ban24_plan.log
less ../stk_daily/$day/ban24_plan.log

