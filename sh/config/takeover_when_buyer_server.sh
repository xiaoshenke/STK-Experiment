#!/bin/bash

if [ $# -ne 1 ]
then
	echo usage sh/config/write_takeover_when_buyer_server.sh val
	exit 1
fi

val=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/properties_cli.py write_takeover_when_buyer_server $val 
python realtime/properties_cli.py write_takeover_when_buyer_server $val

cmd="sh/config/write_takeover_when_buyer_server.sh $val"
sh/log/log_to_operate.sh "$cmd" "TAKEOVER-WHEN-BUYER-SERVER"

