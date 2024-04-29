#!/bin/bash
# usage sh/tail_flush.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/flush.log
echo tail -f ../stk_daily/$day/flush.log
tail -f ../stk_daily/$day/flush.log

