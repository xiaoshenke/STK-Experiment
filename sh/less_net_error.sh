#!/bin/bash
# usage sh/less_net_error.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/net_error.log
echo less ../stk_daily/$day/net_error.log
less ../stk_daily/$day/net_error.log

