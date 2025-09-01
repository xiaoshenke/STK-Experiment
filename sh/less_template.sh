#!/bin/bash
# usage sh/less_template.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/template.log
echo less ../stk_daily/$day/template.log
less ../stk_daily/$day/template.log

