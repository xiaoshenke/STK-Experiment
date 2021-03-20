#!/bin/bash
# usage sh/tail_xls_opener.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/xls_opener.log
echo tail -f ../stk_daily/$day/xls_opener.log
tail -f ../stk_daily/$day/xls_opener.log

