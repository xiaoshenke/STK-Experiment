#!/bin/bash
# usage sh/less_operate.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
	day=$1
fi

touch ../stk_daily/$day/operate.log
echo less ../stk_daily/$day/operate.log
less ../stk_daily/$day/operate.log

