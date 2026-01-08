#!/bin/bash
# usage sh/realtime/buyer_scheduler_clean.sh [clean]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

clean=1
if [ $# -eq 1 ]
then
	clean=$1
fi

echo "设置一下当前的clean模式"

if [ $clean -eq 1 ]
then
	echo sh/config/write_running_mode.sh clean
	sh/config/write_running_mode.sh clean
else
	echo sh/config/write_running_mode.sh default
        sh/config/write_running_mode.sh default
fi
