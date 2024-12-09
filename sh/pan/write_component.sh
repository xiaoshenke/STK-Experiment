#!/bin/bash

if [ $# -ne 1 ]
then
	echo usage sh/config/write_component.sh val
	exit 1
fi

val=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/pan_config_cli.py write_component $val 
python realtime/pan_config_cli.py write_component $val

