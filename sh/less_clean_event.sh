#!/bin/bash
# usage sh/less_clean_event.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/clean_event.log
echo less ../stk_daily/$day/clean_event.log
less ../stk_daily/$day/clean_event.log

