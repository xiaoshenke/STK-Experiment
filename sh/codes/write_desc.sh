#!/bin/bash

# 给某个切片加上message

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
code_type=#
desc=#
group=#
now=0

if [ $# -lt 2 ]
then
	echo Usage: sh/codes/write_message.sh code-type msg [--day ]
      	exit 2
fi

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-reason | --reason | -desc| --desc)
		shift
		desc=$1
		;;
	-group | --group)
		shift
		group=$1
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

echo python realtime/code_type/reg_cli.py write_desc $code_type --day $day $desc 
python realtime/code_type/reg_cli.py write_desc $code_type --day $day $desc --do_log 1

