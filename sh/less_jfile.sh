#!/bin/bash
# usage sh/less_jfile.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
	day=$1
fi

touch ../stk_daily/$day/jfile.log
echo less ../stk_daily/$day/jfile.log
less ../stk_daily/$day/jfile.log

