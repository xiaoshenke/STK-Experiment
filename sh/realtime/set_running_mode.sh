#!/bin/bash
# Usage: sh/realtime/set_running_mode.sh [mode]

mode='light'
if [ $# -eq 1 ]
then
	mode=$1
fi

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

#echo python realtime/observe/bind.py set --running_mode $mode
#python realtime/observe/bind.py set --running_mode $mode

echo python realtime/observe/upstp.py set --running_mode $mode
python realtime/observe/upstp.py set --running_mode $mode

echo python realtime/observe/chaoduan.py set --running_mode $mode
python realtime/observe/chaoduan.py set --running_mode $mode

echo python realtime/observe/buyer.py set --running_mode $mode
python realtime/observe/buyer.py set --running_mode $mode

echo python realtime/observe/xls.py set --running_mode $mode
python realtime/observe/xls.py set --running_mode $mode

#echo python realtime/buyer/observe_cli.py set --running_mode $mode
#python realtime/buyer/observe_cli.py set --running_mode $mode

