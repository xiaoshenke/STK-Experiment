#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
code_type=#
desc=#

now=0
while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	*)
		# set value to type|flush_type by now-flag
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

if [[ $code_type == '#' ]]
then
	echo 没有输入股票池!
	exit 2
fi

echo python realtime/code_type/pan_cli.py add $code_type --day $day --reason $desc
python realtime/code_type/pan_cli.py add $code_type --day $day --reason $desc
