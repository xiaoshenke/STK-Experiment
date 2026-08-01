#!/bin/bash
# usage sh/ls_fenshi.sh [day]


path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

#day=`date +'%Y-%m-%d'`

day=$(python util/sh_util.py get_today)
if [ $# -eq 1 ]
then
	day=$1
fi

echo ls ../stk_daily/$day/fenshi_wholecodes/
ls ../stk_daily/$day/fenshi_wholecodes/
