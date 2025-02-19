#!/bin/bash
# usage sh/buyer/current_branch.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
	day=$1
fi

echo ls ../stk_daily/$day/buyer/|sort
ls ../stk_daily/$day/buyer/|sort
