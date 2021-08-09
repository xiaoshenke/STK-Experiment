#!/bin/bash
# usage sh/tail_stock.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/stock.log
echo tail -f ../stk_daily/$day/stock.log
tail -f ../stk_daily/$day/stock.log

