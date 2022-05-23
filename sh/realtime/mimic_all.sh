#!/bin/bash
# usage sh/mimic_all.sh [mimic]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

mimic=1
if [ $# -eq 1 ]
then
	mimic=$1
fi

echo "将依次对upstp,chaozuo,stocks,pool,longhu,market,xls,bind,buyer,mline,dig组件 进行mimic"

echo python realtime/observe/upstp.py set --mimic $mimic
python realtime/observe/upstp.py set --mimic $mimic

echo python realtime/observe/chaozuo.py set --mimic $mimic
python realtime/observe/chaozuo.py set --mimic $mimic

echo python realtime/observe/stocks.py set --mimic $mimic
python realtime/observe/stocks.py set --mimic $mimic

#echo python realtime/observe/pool.py set --mimic $mimic
#python realtime/observe/pool.py set --mimic $mimic

#echo python realtime/observe/longhu.py set --mimic $mimic
#python realtime/observe/longhu.py set --mimic $mimic

echo python realtime/observe/market.py set --mimic $mimic
python realtime/observe/market.py set --mimic $mimic

echo python realtime/observe/xls.py set --mimic $mimic
python realtime/observe/xls.py set --mimic $mimic

echo python realtime/observe/bind.py set --mimic $mimic
python realtime/observe/bind.py set --mimic $mimic

echo python realtime/observe/longhu.py set --mimic $mimic
python realtime/observe/longhu.py set --mimic $mimic


echo python realtime/buyer/observe_cli.py set --mimic $mimic
python realtime/buyer/observe_cli.py set --mimic $mimic

echo python realtime/observe/mline.py set --mimic $mimic
python realtime/observe/mline.py set --mimic $mimic

echo python realtime/observe/change.py set --mimic $mimic
python realtime/observe/change.py set --mimic $mimic

echo python realtime/observe/dig.py set --mimic $mimic
python realtime/observe/dig.py set --mimic $mimic

#echo python realtime/report_cli.py set --mimic $mimic
#python realtime/report_cli.py set --mimic $mimic
