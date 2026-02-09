#!/bin/bash

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=`date +'%Y-%m-%d'`
code_type=#
desc=#
name=#
mode='plan'
sort=-1
start=#
end=#
flush=1

now=0

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
        -sort | --sort)
		shift
		sort=$1
		;;
        -start | --start)
		shift
		start=$1
		;;
        -end | --end)
		shift
		end=$1
		;;
        -flush | --flush)
		shift
		flush=$1
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

echo python engine/observe/buyer/server/reg_cli.py add $code_type --sort $sort --start $start --end $end --day $day --mode $mode --reason "$desc"
python engine/observe/buyer/server/reg_cli.py add $code_type --flush_now $flush --sort $sort --start $start --end $end --day $day --mode $mode --reason "$desc" 
