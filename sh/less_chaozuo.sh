#!/bin/bash
# usage sh/less_chaozuo.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

echo less ../stk_daily/$day/chaozuo_plan.log
less ../stk_daily/$day/chaozuo_plan.log

