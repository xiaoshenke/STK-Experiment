#!/bin/bash
# usage sh/less_event.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/buyer_req.log
echo less ../stk_daily/$day/buyer_req.log
less ../stk_daily/$day/buyer_req.log

