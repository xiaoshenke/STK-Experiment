#!/bin/bash

echo ATTENTION: FLUSH-CMDS CLI

day=#
time_str=#
mode=#

type=''
flush_type='simple'
front_type=#
fronts_type=#
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
	-fronts | --fronts)
		shift
		fronts_type=$1
		;;
	-ignore_cache | --ignore_cache)
		shift
		ignore_cache=$1
		;;
	-help | --help)
		echo usage sh/realtime/flush_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] type [pull_info|stage:]
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
			#front_type=$1
			fronts_type=$1
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
	#front_type=$3
	fronts_type=$3
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

is_code_types=$(python realtime/flush_cli.py is_code_types $type)
is_eva=$(python realtime/flush_cli.py is_front_type $flush_type)
# reset value to last character
is_eva=${is_eva:0-1:1}

echo "sh/flush_cli.sh is_code_types:$is_code_types is_eva:$is_eva"

if [[ $is_code_types != "1" ]] 
then
	echo $type 不是切片池,当前仅支持切片池类型
	exit 2
fi

if [[ $flush_type =~ "stage:" ]]
then
	echo python realtime/flush_cli.py do_stage $type $flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/flush_cli.py do_stage $type $flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $flush_type =~ "op:" ]] || [[ $flush_type =~ "operate:" ]]
then
	echo python realtime/flush_cli.py do_operate $type $flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/flush_cli.py do_operate $type $flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $flush_type =~ "pull_info" ]] || [[ $flush_type =~ "pullinfo" ]]
then
	echo python realtime/flush_cli.py pull_info $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/flush_cli.py pull_info $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $flush_type == "simple" ]]
then
	echo python realtime/flush_cli.py simple_flush $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/flush_cli.py simple_flush $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $is_code_types == "1" ]] && [[ $is_eva == "1" ]]
then
	echo 不支持code-types+eva类型 不过可以  sh/front_cli.sh $type $flush_type --mode $mode --day $day --time_str $time_str
	exit 2

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

elif [[ $is_eva == "1" ]]
then
	echo python realtime/flush_cli.py flush_front $type $flush_type --fronts $fronts_type --day $day --time_str $time_str --mode $mode
	python realtime/flush_cli.py flush_front $type $flush_type --fronts $fronts_type --day $day --time_str $time_str --mode $mode

#else
#	echo python realtime/flush_cli.py flush_subs $type $flush_type --front_type $front_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
#	python realtime/flush_cli.py flush_subs $type $flush_type --front_type $front_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

fi

