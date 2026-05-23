#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
now=0
start=#
end=#

while [ -n "$1" ]
do 
	case "$1" in 
	-day | --day)
		shift
		day=$1
		;;
	-start | --start)
		shift
		start=$1
		;;
	-end | --end)
		shift
		end=$1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			start=$1
		elif [ $now -eq 1 ]
		then
			end=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

echo python tool/silu/generate_cli.py generate_all --day $day --start $start --end $end
python tool/silu/generate_cli.py generate_all --day $day --start $start --end $end

