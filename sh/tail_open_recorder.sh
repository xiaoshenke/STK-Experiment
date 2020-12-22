#!/bin/bash
# usage sh/less_open_recorder.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/open/cmd.csv
echo tail -f ../stk_daily/$day/open/cmd.csv
tail -f ../stk_daily/$day/open/cmd.csv

