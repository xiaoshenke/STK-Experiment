#!/bin/bash
# usage sh/mimic_all.sh [mimic]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

mimic=1
if [ $# -eq 1 ]
then
	mimic=$1
fi

echo python realtime/observe/stocks.py set --mimic $mimic
python realtime/observe/stocks.py set --mimic $mimic

echo python realtime/observe/pool.py set --mimic $mimic
python realtime/observe/pool.py set --mimic $mimic

echo python realtime/observe/longhu.py set --mimic $mimic
python realtime/observe/longhu.py set --mimic $mimic

echo python realtime/observe/market.py set --mimic $mimic
python realtime/observe/market.py set --mimic $mimic

echo python realtime/observe/xls.py set --mimic $mimic
python realtime/observe/xls.py set --mimic $mimic
