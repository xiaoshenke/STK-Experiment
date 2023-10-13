#!/bin/bash

export PYTHONUNBUFFERED=1

if [ $# -ne 1 ]
then
	echo Usage:sh/run_prerun.sh day
fi

day=$1

echo nohup python engine/crontab/prerun/prerun_job.py run $day >>prerun.log 2>&1 &
nohup python engine/crontab/prerun/prerun_job.py run $day >>prerun.log 2>&1 &

