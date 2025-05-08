#!/bin/bash
# Usage: sh/realtime/caozuo_running_mode.sh [mode]

mode='light'
if [ $# -eq 1 ]
then
	mode=$1
fi

echo python realtime/observe/caozuo.py set --running_mode $mode
python realtime/observe/caozuo.py set --running_mode $mode

