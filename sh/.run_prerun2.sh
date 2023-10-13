#!/bin/bash

if [ $# -ne 1 ]
then
	echo Usage:sh/run_prerun2.sh day
fi

day=$1

echo nohup python engine/crontab/build/prerun2_job.py run $day >>prerun2.log 2>&1 &
nohup python engine/crontab/build/prerun2_job.py run $day >>prerun2.log 2>&1 &

