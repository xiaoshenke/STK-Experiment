#!/bin/bash
# usage sh/less_flush.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/flush.log
echo less ../stk_daily/$day/flush.log
less ../stk_daily/$day/flush.log

