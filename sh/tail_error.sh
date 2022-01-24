#!/bin/bash
# usage sh/tail_error.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/error.log
echo tail -f ../stk_daily/$day/error.log
tail -f ../stk_daily/$day/error.log

