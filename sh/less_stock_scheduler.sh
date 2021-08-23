#!/bin/bash
# usage sh/less_stock_scheduler.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/stock_scheduler.log
echo less ../stk_daily/$day/stock_scheduler.log
less ../stk_daily/$day/stock_scheduler.log

