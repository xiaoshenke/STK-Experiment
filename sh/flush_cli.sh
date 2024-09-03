#!/bin/bash

echo ATTENTION: FLUSH-CMDS CLI

day=#
time_str=#
mode=#

type=''
flush_type='buy'
front_type=#
ignore_cache=0

now=0
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
	-eva | --eva | --front | -front | --front_type | -front_type)
		shift
		front_type=$1
		;;
	-ignore_cache | --ignore_cache)
		shift
		ignore_cache=$1
		;;
	-help | --help)
		echo usage sh/realtime/flush_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] type
		exit 1
		;;
	*)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		elif [ $now -eq 1 ]
		then
			flush_type=$1
		else
			front_type=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

if [ $# -eq 1 ]
then
	type=$1
fi

if [ $# -eq 2 ]
then
	type=$1
	flush_type=$2
fi

if [ $# -eq 3 ]
then
	type=$1
	flush_type=$2
	front_type=$3
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

is_code_types=$(python realtime/flush_cli.py is_code_types $type)

if [[ $type == "evaed" ]]
then
	echo python realtime/flush_cli.py flush $type --day $day --time_str $time_str --mode $mode --flush_type $flush_type --ignore_cache $ignore_cache
	python realtime/flush_cli.py flush $type --day $day --time_str $time_str --mode $mode --flush_type $flush_type --ignore_cache $ignore_cache

elif [[ $is_code_types == "1" ]]
then
	echo python realtime/flush_cli.py flush $type --day $day --time_str $time_str --mode $mode --flush_type $flush_type --ignore_cache $ignore_cache
        python realtime/flush_cli.py flush $type --day $day --time_str $time_str --mode $mode --flush_type $flush_type --ignore_cache $ignore_cache

elif [[ $flush_type == "simple" ]] || [[ $flush_type == "simple_pull" ]] || [[ $flush_type == "zhendang" ]] || [[ $flush_type == "maichong" ]]
then
	echo python realtime/flush_cli.py flush $type --day $day --time_str $time_str --mode $mode --flush_type $flush_type --ignore_cache $ignore_cache
	python realtime/flush_cli.py flush $type --day $day --time_str $time_str --mode $mode --flush_type $flush_type --ignore_cache $ignore_cache

#elif [[ ${flush_type::-2} == "ss" ]]
elif [[ $flush_type == *ss ]]
then
	echo python realtime/flush_cli.py flush_fronts $type $flush_type --day $day --time_str $time_str --mode $mode
	python realtime/flush_cli.py flush_fronts $type $flush_type --day $day --time_str $time_str --mode $mode 

elif [[ $flush_type =~ "buy" ]]
then
	echo python realtime/flush_cli.py flush_buy $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/flush_cli.py flush_buy $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $flush_type =~ "itrend" ]] || [[ $flush_type =~ "trend2" ]]
then
	echo python realtime/flush_cli.py flush_itrend $type --itrend_str $flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/flush_cli.py flush_itrend $type --itrend_str $flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $flush_type =~ "pull" ]]
then
	echo python realtime/flush_cli.py pull $type --flush_type $flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/flush_cli.py pull $type --flush_type $flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

else
	echo python realtime/flush_cli.py flush_subs $type $flush_type --front_type $front_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/flush_cli.py flush_subs $type $flush_type --front_type $front_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

fi

