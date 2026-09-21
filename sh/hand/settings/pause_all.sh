#!/bin/bash

if [ $# -ne 1 ]
then
	echo usage sh/hand/settings/pause_all.sh val
	exit 1
fi

val=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

key="hand.pause_all"

echo python realtime/properties_cli.py write_key_val $key $val 
python realtime/properties_cli.py write_key_val $key $val 

