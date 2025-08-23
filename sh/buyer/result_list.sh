#!/bin/bash

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

echo "ls ../stk_daily/$day/buyer//  |grep Run|grep Temp"
ls ../stk_daily/$day/buyer//|grep Run |grep Temp

echo ""
echo "open \"../stk_daily/$day/buyer/\""
echo "open ../stk_daily/$day/buyer/"

