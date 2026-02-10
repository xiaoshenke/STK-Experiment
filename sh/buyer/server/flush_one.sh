#!/bin/bash

# Usage: sh/buyer/server/flush_one.sh id

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`

if [ $# -lt 1 ]
then
	echo Usage: sh/buyer/server/flush_one.sh id
	exit 2
fi

id=#

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		id=$1
		;;
	esac
	shift
done


echo python engine/observe/buyer/server/web_cli.py trigger_id $id
python engine/observe/buyer/server/web_cli.py trigger_id $id

