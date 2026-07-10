#!/bin/bash

if [ $# -lt 1 ]
then
	echo Usage: sh/buyer/add_buyer.sh xx "[reason|desc]"
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
			msg="$1"
		elif [ $now -eq 1 ]
		then 
			chain_id=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python engine/recorder/chain/cli.py start "$msg" --chain_id $chain_id --day $day --mode $mode --time_str $time_str
python engine/recorder/chain/cli.py start "$msg" --chain_id $chain_id --day $day --mode $mode --time_str $time_str

