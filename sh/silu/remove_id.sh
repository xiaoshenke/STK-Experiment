#!/bin/bash
# usage sh/silu/remove_id.sh ABC

# 删除一些自己觉得效果不好的数据

if [ $# -lt 1 ]
then
	echo usage sh/silu/remove_id.sh ABC
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
		echo usage sh/silu/remove_id.sh ABC [day]
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

echo python tool/silu/reg_cli.py remove_id $id --day $day
python tool/silu/reg_cli.py remove_id $id --day $day
