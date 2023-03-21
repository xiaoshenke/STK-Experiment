#!/bin/bash

mimic=0
if [ $# -eq 1 ]
then
	mimic=$1
fi

export PYTHONUNBUFFERED=1

echo nohup python engine/report/plan/cli.py start_plan_reporter_engine_mode --mimic_open_code $mimic

nohup python engine/report/plan/cli.py start_plan_reporter_engine_mode --mimic_open_code $mimic >>reporter.log 2>&1 &
