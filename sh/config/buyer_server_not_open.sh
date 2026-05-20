#!/bin/bash

if [ $# -ne 1 ]
then
	echo usage sh/config/write_buyer_server_not_open.sh val
	exit 1
fi

val=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/properties_cli.py write_buyer_server_not_open $val 
python realtime/properties_cli.py write_buyer_server_not_open $val

cmd="sh/config/write_buyer_server_not_open.sh $val"
sh/log/log_to_operate.sh "$cmd" "WRITE-BUYER-SERVER-NOT-OPEN"

