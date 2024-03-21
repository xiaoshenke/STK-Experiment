#!/bin/bash
# usage sh/tail_zao_observe.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/zao_observe.log
echo tail -f ../stk_daily/$day/zao_observe.log
tail -f ../stk_daily/$day/zao_observe.log

