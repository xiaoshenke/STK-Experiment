#!/bin/bash

# Usage: sh/buyer/buyer_list.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`

if [ $# -eq 1 ]
then
	day=$1
fi

echo python engine/observe/buyer/reg_cli.py last --day $day 
python engine/observe/buyer/reg_cli.py last --day $day
