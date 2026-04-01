#!/bin/bash

if [ $# -ne 1 ]
then
	echo usage sh/config/write_use_pool.sh val
	exit 1
fi

val=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/properties_cli.py write_use_pool $val 
python realtime/properties_cli.py write_use_pool $val

