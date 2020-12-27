#!/bin/bash
# usage sh/tail_pretraces_list.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/pretraces_list.log
echo less ../stk_daily/$day/pretraces_list.log
less ../stk_daily/$day/pretraces_list.log

