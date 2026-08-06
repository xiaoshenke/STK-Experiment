#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
code_type=#
now=0
add=0
mode='now'
flush_mode='memory'
operate='flush'
time_str='0'

if [ $# -lt 1 ]
then
	echo Usage: sh/xls/entity/master.sh code_type [--day ] 
      	exit 2
fi

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
	-operate | --operate)
		shift
		operate=$1
		;;
	-flush_mode | --flush_mode)
		shift
		flush_mode=$1
		;;

	-add | --add_codes | --add)
		shift
		add=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			code_type="$1"
		elif [ $now -eq 1 ]
		then
			flush_mode=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python engine/xls/runner/cli.py run $code_type master --flush_mode $flush_mode --day $day --time_str $time_str --mode $mode
python engine/xls/runner/cli.py run $code_type master --flush_mode $flush_mode --day $day --time_str $time_str --mode $mode 
