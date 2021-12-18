#!/bin/bash
# usage sh/tail_reporter.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
        day=$1
fi

touch ../stk_daily/$day/report_recorder.log
echo tail -f ../stk_daily/$day/report_recorder.log
tail -f ../stk_daily/$day/report_recorder.log

