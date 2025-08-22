#!/bin/bash

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

echo "ls ../stk_daily/$day/caozuo//  |grep RunTemp"
ls ../stk_daily/$day/caozuo//|grep RunTemp

echo ""
echo "open \"../stk_daily/$day/caozuo/\""
echo "open ../stk_daily/$day/caozuo/"

