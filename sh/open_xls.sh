#!/bin/bash
# usage sh/open_xls.sh ABC

day=`date +'%Y-%m-%d'`

if [ $# -lt 1 ]
then
	echo usage sh/open_xls.sh ABC
	exit 2
fi

xls=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/caop/xls/info/xueqiu_info.py get $xls $day 09:00:00 --open 1
python engine/caop/xls/info/xueqiu_info.py get $xls $day 09:00:00 --open 1

