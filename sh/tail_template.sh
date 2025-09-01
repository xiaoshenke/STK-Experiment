#!/bin/bash
# usage sh/tail_template.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/template.log
echo tail -f ../stk_daily/$day/template.log
tail -f ../stk_daily/$day/template.log

