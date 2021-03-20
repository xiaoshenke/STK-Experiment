#!/bin/bash
# usage sh/less_xls_opener.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

echo less ../stk_daily/$day/xls_opener.log
less ../stk_daily/$day/xls_opener.log

