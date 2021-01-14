#!/bin/bash
# usage sh/less_manual.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

echo less ../stk_daily/$day/manual_list.log
less ../stk_daily/$day/manual_list.log

