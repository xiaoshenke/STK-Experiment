#!/bin/bash
# usage sh/less_market_observer.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

echo less ../stk_daily/$day/market_observer.log
less ../stk_daily/$day/market_observer.log

