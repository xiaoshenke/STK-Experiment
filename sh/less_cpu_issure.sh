#!/bin/bash
# usage sh/less_cpu_issure.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/cpu_issure.log
echo less ../stk_daily/$day/cpu_issure.log
less ../stk_daily/$day/cpu_issure.log

