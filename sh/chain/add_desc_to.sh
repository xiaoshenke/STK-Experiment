#!/bin/bash

if [ $# -lt 2 ]
then
	echo Usage: sh/chain/add_desc_to.sh id msg | sh/chain/add_desc_to.sh msg id ->也就是这俩的顺序可以打乱
	exit 2
fi

day=`date +'%Y-%m-%d'`
code_type=#
desc=#
name=#
now=0
mode='now'
msg='0'
time_str='0'
print_run_msg=0
flush=0
force=0
chain_id=-1

chain_id_is_set=0

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-mode | --mode)
		shift
		mode=$1
		;;
	-time_str | --time_str)
		shift
		time_str=$1
		;;
	-chain_id | --chain_id | --chain)
		shift
		chain_id=$1
		;;
	-flush | --flush)
		shift
		flush=$1
		;;
	-force | --force)
		shift
		force=$1
		;;
	-print_run_msg | --print_run_msg)
		shift
		print_run_msg=$1
		;;
	-reason | --reason | -desc| --desc)
		shift
		desc=$1
		;;
	-name | --name)
		shift
		name=$1
		;;
	*)
		if [ $now -eq 0 ]
		then
			is_id=$(python engine/recorder/chain/cli.py is_single_id $1)
			if [[ $is_id == "1" ]]
			then
				chain_id=$1
				chain_id_is_set=1
			else
				msg="$1"
			fi
		elif [ $now -eq 1 ]
		then 
			if [ $chain_id_is_set -eq 1 ]
			then
				msg="$1"
			else
				chain_id=$1
			fi
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/recorder/chain/cli.py add_desc $chain_id "$msg" --day $day --mode $mode --time_str $time_str
python engine/recorder/chain/cli.py add_desc $chain_id "$msg" --day $day --mode $mode --time_str $time_str

