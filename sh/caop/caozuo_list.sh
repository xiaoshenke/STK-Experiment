#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
now=0
xls='0'

if [ $# -eq 1 ]
then
	day=$1
fi

echo ls /Users/wuxian/Desktop/stk_daily/$day/caozuo
find /Users/wuxian/Desktop/stk_daily/$day/caozuo|grep -v download

