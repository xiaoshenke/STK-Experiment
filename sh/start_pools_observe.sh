#!/bin/bash

# Usage: sh/start_pools_observe.sh [mode]

export PYTHONUNBUFFERED=1

mode='change'
if [ $# -eq 1 ]
then
	mode=$1
fi

echo nohup python engine/observe/pools/cli.py start_engine_mode --running_mode $mode --mimic_open true 
nohup python engine/observe/pools/cli.py start_engine_mode --running_mode $mode --mimic_open true >>observe.pools.log 2>&1 &


