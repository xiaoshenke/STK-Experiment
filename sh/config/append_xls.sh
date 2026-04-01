#!/bin/bash

if [ $# -ne 1 ]
then
	echo usage sh/config/write_append_xls.sh val
	exit 1
fi

val=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/properties_cli.py write_append_xls $val 
python realtime/properties_cli.py write_append_xls $val

