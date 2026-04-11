#!/bin/bash
# usage sh/buyer/server/remove_id.sh ABC

if [ $# -lt 1 ]
then
	echo usage sh/buyer/server/remove_id.sh ABC
	exit 2
fi

id='-1'
day=#

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
		echo usage sh/buyer/server/remove_id.sh ABC [day]
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

echo python engine/observe/buyer/server/reg_cli.py remove_id $id $day
python engine/observe/buyer/server/reg_cli.py remove_id $id --day $day

