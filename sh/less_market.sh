#!/bin/bash
# usage sh/less_market.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

echo less ../stk_daily/$day/market.log
less ../stk_daily/$day/market.log

