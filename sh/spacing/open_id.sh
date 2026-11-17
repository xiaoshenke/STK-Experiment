#!/bin/bash
# usage sh/buyer/server/open_by_schedule_id.sh ABC

if [ $# -lt 1 ]
then
	echo usage sh/spacing/open_id.sh xx
	exit 2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=$(python util/sh_util.py get_today)

id='-1'

now=0
while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-id | --id)
		shift
		id=$1
		;;
	-help | --help)
		echo usage sh/spacing/open_id.sh xx
		exit 1
		;;
	*)
		if [ $now -eq 0 ]
		then
			id=$1
		elif [ $now -eq 1 ]
		then
			day=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/spacing/open_cli.py open_by_id $id --day $day
python engine/spacing/open_cli.py open_by_id $id --day $day
