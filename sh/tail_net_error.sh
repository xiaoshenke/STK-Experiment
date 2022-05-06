#!/bin/bash
# usage sh/tail_net_error.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/net_error.log
echo tail -f ../stk_daily/$day/net_error.log
tail -f ../stk_daily/$day/net_error.log

