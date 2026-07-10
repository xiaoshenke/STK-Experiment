#!/bin/bash
# usage sh/chain/file.sh [day]

day=`date +'%Y-%m-%d'`
if [ $# -eq 1 ]
then
	day=$1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/recorder/chain/cli.py file --day $day
python engine/recorder/chain/cli.py file --day $day
