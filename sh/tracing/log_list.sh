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

echo ls /Users/wuxian/Desktop/stk_daily/$day/|grep observe|grep xx_|grep log
ls /Users/wuxian/Desktop/stk_daily/$day/|grep observe|grep xx_|grep log

