#!/bin/bash

if [ $# -ne 1 ]
then
	echo Usage:sh/run_build.sh day
fi
export PYTHONUNBUFFERED=1

day=$1

echo nohup python engine/crontab/build/build_job.py run $day >>build.log 2>&1 &
nohup python engine/crontab/build/build_job.py run $day >>build.log 2>&1 &

