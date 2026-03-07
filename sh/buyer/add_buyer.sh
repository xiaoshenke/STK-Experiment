#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

if [ $# -lt 1 ]
then
	echo Usage: sh/buyer/add_buyer.sh xx [name] [reason]
	exit 2
fi

day=`date +'%Y-%m-%d'`
code_type=#
desc=#
name=#
now=0
mode='plan'
print_run_msg=0

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
			code_type=$1
		elif [ $now -eq 1 ]
		then 
			desc=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python engine/observe/buyer/reg_cli.py add $code_type --name $name --day $day --mode $mode --reason "$desc" --print_run_msg $print_run_msg
python engine/observe/buyer/reg_cli.py add $code_type --name $name --day $day --mode $mode --reason "$desc" --print_run_msg $print_run_msg
