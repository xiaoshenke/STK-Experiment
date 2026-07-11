#!/bin/bash

# Usage: sh/list/code_type.sh [day]

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

if [ $# -lt 1 ]
then
	echo Usage: sh/chain/print_id.sh xx
	exit 2
fi

day=`date +'%Y-%m-%d'`
time_str='0'
now=0
id=-1

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-time_str | --time_str)
		shift
		time_str=$1
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

echo python engine/recorder/chain/cli.py query_id_and_gene_simple_info $id --day $day 
python engine/recorder/chain/cli.py query_id_and_gene_simple_info $id --day $day
