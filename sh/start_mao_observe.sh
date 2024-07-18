#!/bin/bash

echo Usage: sh/start_mao_observe.sh [xls]

xls=#
if [ $# -eq 1 ]
then
	xls=$1
fi

export PYTHONUNBUFFERED=1

echo nohup python engine/observe/mao/cli.py start_engine_mode --xls $xls
nohup python engine/observe/mao/cli.py start_engine_mode --mimic_open false --xls $xls >>observe.mao.log 2>&1 &

