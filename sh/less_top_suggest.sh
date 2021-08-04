#!/bin/bash
# usage sh/less_top_suggest.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/top_suggest.log
echo less ../stk_daily/$day/top_suggest.log
less ../stk_daily/$day/top_suggest.log

