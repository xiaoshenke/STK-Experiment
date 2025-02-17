#!/bin/bash
# Usage: sh/realtime/set_running_mode.sh [mode]

mode='light'
if [ $# -eq 1 ]
then
	mode=$1
fi

echo python realtime/properties_cli.py write_running_mode $mode
python realtime/properties_cli.py write_running_mode $mode

echo python realtime/observe/mline.py set --running_mode $mode
python realtime/observe/mline.py set --running_mode $mode

echo python realtime/observe/change.py set --running_mode $mode
python realtime/observe/change.py set --running_mode $mode

echo python realtime/observe/market.py set --running_mode $mode
python realtime/observe/market.py set --running_mode $mode

echo python realtime/observe/mao.py set --running_mode $mode
python realtime/observe/mao.py set --running_mode $mode

echo python realtime/observe/pools.py set --running_mode $mode
python realtime/observe/pools.py set --running_mode $mode

echo python realtime/observe/code_types.py set --running_mode $mode
python realtime/observe/code_types.py set --running_mode $mode

echo python realtime/observe/upstp.py set --running_mode $mode
python realtime/observe/upstp.py set --running_mode $mode

echo python realtime/observe/chaoduan.py set --running_mode $mode
python realtime/observe/chaoduan.py set --running_mode $mode

#echo python realtime/observe/buyer.py set --running_mode $mode
#python realtime/observe/buyer.py set --running_mode $mode

echo python engine/scheduler/buyer/buyer.py set --running_mode $mode
python engine/scheduler/buyer/buyer.py set --running_mode $mode

echo python realtime/observe/xls.py set --running_mode $mode
python realtime/observe/xls.py set --running_mode $mode

echo python realtime/observe/jingjia.py set --running_mode $mode
python realtime/observe/jingjia.py set --running_mode $mode

echo python realtime/observe/pan.py set --running_mode $mode
python realtime/observe/pan.py set --running_mode $mode

