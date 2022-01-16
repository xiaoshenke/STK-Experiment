#!/bin/bash
# usage sh/tail_event.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/event.log
echo tail -f ../stk_daily/$day/event.log
tail -f ../stk_daily/$day/event.log

