#!/bin/bash

#echo "$@"
if [ $# -ne 1 ]
then
	echo usage: sh/openid.sh 123
	exit 0
fi

id=$1

echo python realtime/query_cli.py open $id
python realtime/query_cli.py open $id

