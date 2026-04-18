#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
time_str=#
code_type=#
fronts_type='rup'
desc=#
group=#
now=0
mode='now'

if [ $# -lt 1 ]
then
	echo Usage: sh/codes/find_fronts.sh code-type [fronts-type]
      	exit 2
fi

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
	-mode | --mode)
		shift
		mode=$1
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
			fronts_type=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

cmd="sh/codes/find_fronts.sh $code_type $fronts_type --day $day --mode $mode --time_str $time_str"
sh/log/log_to_operate.sh "$cmd" "CODES-FIND-FRONTS"

echo python python realtime/caop/code_type.py find_fronts $code_type $fronts_type --day $day --mode $mode --time_str $time_str
python realtime/caop/code_type.py find_fronts $code_type $fronts_type --day $day --mode $mode --time_str $time_str

