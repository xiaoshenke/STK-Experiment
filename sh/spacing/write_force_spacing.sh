#!/bin/bash

if [ $# -ne 1 ]
then
	echo usage sh/spacing/write_force_spacing.sh val
	exit 1
fi

val=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/spacing_config_cli.py write_force_spacing $val 
python realtime/spacing_config_cli.py write_force_spacing $val

