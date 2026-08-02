#!/bin/bash
# usage sh/chain/file.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=$(python util/sh_util.py get_today)

if [ $# -eq 1 ]
then
	day=$1
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/recorder/chain/cli.py file --day $day
python engine/recorder/chain/cli.py file --day $day
