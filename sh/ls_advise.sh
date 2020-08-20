#!/bin/bash
# usage sh/ls_advise.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
	day=$1
fi

echo ls ../stk_daily/$day/advise
ls ../stk_daily/$day/advise

