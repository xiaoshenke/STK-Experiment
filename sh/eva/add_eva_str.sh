#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
code_type=#
desc=#
name=#
now=0
mode='plan'

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

echo python engine/eva_str/reg_cli.py add $code_type --name $name --day $day --mode $mode --reason "$desc"
python engine/eva_str/reg_cli.py add $code_type --name $name --day $day --mode $mode --reason "$desc" 
