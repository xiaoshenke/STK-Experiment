#!/bin/bash
# usage sh/less_last_trade.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/last_trade.log
echo less ../stk_daily/$day/last_trade.log
less ../stk_daily/$day/last_trade.log

