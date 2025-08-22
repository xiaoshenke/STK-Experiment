#!/bin/bash

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

echo "剧本调度列表"
echo "find /Users/wuxian/Desktop/stk_daily/$day//observe//|grep JubenObser"
find /Users/wuxian/Desktop/stk_daily/$day//observe//|grep JubenObser
