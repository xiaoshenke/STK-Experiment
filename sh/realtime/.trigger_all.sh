#!/bin/bash
# usage sh/trigger_all.sh

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/observe/stocks.py trigger
python realtime/observe/stocks.py trigger

echo python realtime/observe/pool.py trigger
python realtime/observe/pool.py trigger

echo python realtime/observe/longhu.py trigger
python realtime/observe/longhu.py trigger

echo python realtime/observe/market.py trigger
python realtime/observe/market.py trigger

echo python realtime/observe/xls.py trigger
python realtime/observe/xls.py trigger
