#!/bin/bash
# usage sh/less_stock.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

echo less ../stk_daily/$day/stock.log
less ../stk_daily/$day/stock.log

