#!/bin/bash
# usage sh/tail_top_suggest.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/top_suggest.log
echo tail -f ../stk_daily/$day/top_suggest.log
tail -f ../stk_daily/$day/top_suggest.log

