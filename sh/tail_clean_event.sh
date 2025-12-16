#!/bin/bash
# usage sh/tail_clean_event.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/clean_event.log
echo tail -f ../stk_daily/$day/clean_event.log
tail -f ../stk_daily/$day/clean_event.log

