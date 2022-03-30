#!/bin/bash
# usage sh/open_last_all.sh

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/observe/market.py open_last
python realtime/observe/market.py open_last

echo python realtime/observe/stocks.py open_last
python realtime/observe/stocks.py open_last

echo python realtime/observe/pool.py open_last
python realtime/observe/pool.py open_last

echo python realtime/observe/upstp.py open_last
python realtime/observe/upstp.py open_last

#echo python realtime/observe/longhu.py open_last
#python realtime/observe/longhu.py open_last

echo python realtime/observe/bind.py open_last
python realtime/observe/bind.py open_last

echo python realtime/observe/xls.py open_last
python realtime/observe/xls.py open_last



