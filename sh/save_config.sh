#!/bin/bash
# save realtime/realtime.properties to ../stk_daily/$day 

# usage sh/save_config.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
	day=$1
fi

echo cp realtime/realtime.properties ../stk_daily/$day/
cp realtime/realtime.properties ../stk_daily/$day/

echo cp realtime/pan.properties ../stk_daily/$day/
cp realtime/pan.properties ../stk_daily/$day/

