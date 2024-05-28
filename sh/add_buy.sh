#!/bin/bash
# usage sh/add_buy.sh ABC

if [ $# -lt 1 ]
then
	echo usage sh/add_buy.sh ABC
	exit 2
fi

code_type=$1

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/code_type/cli.py add_buy $code_type
python realtime/code_type/cli.py add_buy $code_type
