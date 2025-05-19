#!/bin/bash
# usage sh/pan/trigger.sh [type]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

type='default'
if [ $# -eq 1 ]
then
	type=$1
fi


echo python realtime/observe/pan.py trigger --type $type
python realtime/observe/pan.py trigger --type $type
