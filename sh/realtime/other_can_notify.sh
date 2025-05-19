#!/bin/bash
# usage sh/realtime/other_can_notify.sh [can_notify]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

can_notify=1
if [ $# -eq 1 ]
then
	can_notify=$1
fi

echo "对caozuo observe进行can_notify设置操作."

if [ $can_notify -eq 1 ]
then
	echo python realtime/observe/caozuo.py set --running_mode light
	python realtime/observe/caozuo.py set --running_mode light
else
	echo python realtime/observe/caozuo.py set --running_mode default
	python realtime/observe/caozuo.py set --running_mode default
fi
