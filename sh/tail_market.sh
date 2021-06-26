#!/bin/bash
# usage sh/tail_market.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/market.log
echo tail -f ../stk_daily/$day/market.log
tail -f ../stk_daily/$day/market.log

