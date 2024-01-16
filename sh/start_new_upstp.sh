#!/bin/bash

mimic=0
if [ $# -eq 1 ]
then
	mimic=$1
fi

export PYTHONUNBUFFERED=1

echo nohup python engine/observe/upstp/new_cli.py start_engine_mode --mimic_open $mimic

nohup python engine/observe/upstp/new_cli.py start_engine_mode --mimic_open $mimic >>observe.upstp.log 2>&1 &

