#!/bin/bash
# usage sh/ls_apply.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
	day=$1
fi

ls ../stk_daily/$day/fenshi_wholecodes/
