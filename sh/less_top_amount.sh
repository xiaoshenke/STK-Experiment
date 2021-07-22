#!/bin/bash
# usage sh/less_top_amount.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/top_amount.log
echo less ../stk_daily/$day/top_amount.log
less ../stk_daily/$day/top_amount.log

