#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
code_type=#
codes=#
desc=#
rec='default'

now=0
while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-rec | --rec)
		shift
		rec=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			code_type=$1
		elif [ $now -eq 1 ]
		then
			codes=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

if [[ $rec == "tmp" ]]
then
	echo python realtime/code_type/tmp_cli.py add_manual $code_type $codes --day $day 
	python realtime/code_type/tmp_cli.py add_manual $code_type $codes --day $day 
	exit 2
fi
echo python realtime/code_type/reg_cli.py add_manual $code_type $codes --day $day 
python realtime/code_type/reg_cli.py add_manual $code_type $codes --day $day 

