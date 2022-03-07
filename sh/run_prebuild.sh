#!/bin/bash

if [ $# -ne 1 ]
then
	echo Usage:sh/run_prebuild.sh day
fi

day=$1

echo nohup python engine/crontab/build/prebuild_job.py run $day >>prebuild.log 2>&1 &
nohup python engine/crontab/build/prebuild_job.py run $day >>prebuild.log 2>&1 &

