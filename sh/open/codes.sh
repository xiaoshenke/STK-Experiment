#!/bin/bash

if [ $# -lt 1 ]
then
	echo Usage: ./open_codes.sh aaa,bbb,ccc
	exit 2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

codes=$1

echo python realtime/code/cli.py open $codes
python realtime/code/cli.py open $codes

