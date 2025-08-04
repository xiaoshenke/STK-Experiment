#!/bin/bash
# usage sh/pan/trigger.sh [type]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

type='flush'
if [ $# -eq 1 ]
then
	type=$1
fi


echo python realtime/observe/oeva.py trigger --type $type
python realtime/observe/oeva.py trigger --type $type
