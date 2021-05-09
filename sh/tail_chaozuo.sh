#!/bin/bash
# usage sh/tail_chaozuo.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/chaozuo_plan.log
echo tail -f ../stk_daily/$day/chaozuo_plan.log
tail -f ../stk_daily/$day/chaozuo_plan.log

