#!/bin/bash
# usage sh/tail_operate.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/operate.log
echo tail -f ../stk_daily/$day/operate.log
tail -f ../stk_daily/$day/operate.log

