#!/bin/bash

# Usage: sh/message/list_all.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`

if [ $# -eq 1 ]
then
	day=$1
fi

echo python realtime/message_cli.py last --day $day
python realtime/message_cli.py last --day $day

echo file:
python realtime/message_cli.py file --day $day
