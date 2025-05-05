#!/bin/bash

# Usage: sh/start_caozuo_observe.sh [mode]

export PYTHONUNBUFFERED=1

mode='default'
if [ $# -eq 1 ]
then
	mode=$1
fi

echo nohup python engine/observe/caozuo/cli.py start_engine_mode --running_mode $mode --mimic_open true 
nohup python engine/observe/caozuo/cli.py start_engine_mode --running_mode $mode --mimic_open true >>observe.caozuo.log 2>&1 &


