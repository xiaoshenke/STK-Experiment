#!/bin/bash

# 配置keep窗口的策略 比如可以配置成 least(保留最少的window) less default max

if [ $# -ne 1 ]
then
	echo usage sh/config/write_keep_window.sh val
	exit 1
fi

val=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/properties_cli.py write_keep_window $val 
python realtime/properties_cli.py write_keep_window $val

cmd="sh/config/write_keep_window.sh $val"
sh/log/log_to_operate.sh "$cmd" "WRITE-KEEP-WINDOW"

