#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
code_type=#

if [ $# -lt 1 ]
then
	echo Usage: sh/list/code_type.sh [code-type]
	exit 2
fi

if [ $# -eq 1 ]
then
	code_type=$1
elif [ $# -gt 1 ]
then
	code_type=$1
	day=$2
fi

echo python realtime/code_type/reg_cli.py add $code_type --day $day
python realtime/code_type/reg_cli.py add $code_type --day $day
