#!/bin/bash

if [ $# -lt 1 ]
then
	echo Usage: ./get_xls.sh code
	exit 2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

code=$1

echo python realtime/code/cli.py get_xls $code
python realtime/code/cli.py get_xls $code

