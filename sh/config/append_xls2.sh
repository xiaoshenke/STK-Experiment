#!/bin/bash

if [ $# -ne 1 ]
then
	echo usage sh/config/write_append_xls2.sh val
	exit 1
fi

val=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/properties_cli.py write_append_xls2 $val 
python realtime/properties_cli.py write_append_xls2 $val

