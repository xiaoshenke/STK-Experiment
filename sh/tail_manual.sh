#!/bin/bash
# usage sh/tail_manual.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/manual_list.log
echo tail -f ../stk_daily/$day/manual_list.log
tail -f ../stk_daily/$day/manual_list.log

