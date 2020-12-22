#!/bin/bash
# usage sh/less_open_recorder.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/open/cmd.csv
echo less ../stk_daily/$day/open/cmd.csv
less ../stk_daily/$day/open/cmd.csv

