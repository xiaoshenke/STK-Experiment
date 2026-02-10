#!/bin/bash

# Usage: sh/juben/juben_list.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`

if [ $# -eq 1 ]
then
	day=$1
fi

echo find ../stk_daily/$day/juben/
find ../stk_daily/$day/juben/ | grep properties

echo ""
echo find ../stk_daily/$day/buyer/
find ../stk_daily/$day/buyer/ | grep properties

