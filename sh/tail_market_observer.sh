#!/bin/bash
# usage sh/tail_market_observer.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/market_observer.log
echo tail -f ../stk_daily/$day/market_observer.log
tail -f ../stk_daily/$day/market_observer.log

