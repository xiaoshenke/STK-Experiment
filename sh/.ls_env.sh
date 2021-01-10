#!/bin/bash
# usage sh/ls_env.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
	day=$1
fi

echo ls ../stk_daily/$day/env
ls ../stk_daily/$day/env

