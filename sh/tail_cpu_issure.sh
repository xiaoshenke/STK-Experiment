#!/bin/bash
# usage sh/tail_cpu_issure.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/cpu_issure.log
echo tail -f ../stk_daily/$day/cpu_issure.log
tail -f ../stk_daily/$day/cpu_issure.log

