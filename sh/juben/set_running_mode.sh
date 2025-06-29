#!/bin/bash
# Usage: sh/realtime/set_running_mode.sh [mode]

mode='default'
if [ $# -eq 1 ]
then
	mode=$1
fi

echo python realtime/observe/buyer.py set --running_mode $mode
python realtime/observe/buyer.py set --running_mode $mode

