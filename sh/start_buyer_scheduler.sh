#!/bin/bash

export PYTHONUNBUFFERED=1

mimic=0
if [ $# -eq 1 ]
then
	mimic=$1
fi

echo python engine/scheduler/buyer/cli.py start_engine_mode --mimic_open $mimic 
nohup python engine/scheduler/buyer/cli.py start_engine_mode --debug 0 --mimic_open $mimic >>scheduler.buyer.log 2>&1 &

