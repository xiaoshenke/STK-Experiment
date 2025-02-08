#!/bin/bash

echo ATTENTION: FLUSH-CMDS CLI

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=#
time_str=#
mode=#

type=''
# update 2025-02-07: simple->trend
flush_type='trend'
front_type=#
operate='info'
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
		#echo usage sh/realtime/flush_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] type [pull_info|stage:]
		python realtime/flush_cli.py help
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
			operate=$1
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

is_code_types=$(python realtime/flush_cli.py is_code_types $type)
# reset value to last character
is_code_types=${is_code_types:0-1:1}

is_eva=$(python realtime/flush_cli.py is_front_type $flush_type)
# reset value to last character
is_eva=${is_eva:0-1:1}

is_operate=$(python realtime/flush_cli.py is_valid_operate $flush_type)

echo "sh/flush_cli.sh is_code_types:$is_code_types is_eva:$is_eva is_operate:$is_operate"

if [[ $is_code_types != "1" ]] 
then
	echo $type 不是切片池,当前仅支持切片池类型
	exit 2
fi

# 特殊处理fronts fenbu
if [[ $flush_type =~ "stage:" ]] || [[ $flush_type =~ "fronts_fenbu:" ]] || [[ $flush_type =~ "frontsfenbu:" ]]
then
	echo python realtime/flush_cli.py do_stage $type $flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/flush_cli.py do_stage $type $flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $is_operate == "1" ]]
then
	echo python realtime/flush_cli.py do_operate $type op:$flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/flush_cli.py do_operate $type op:$flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $flush_type =~ "op:" ]] || [[ $flush_type =~ "operate:" ]]
then
	echo python realtime/flush_cli.py do_operate $type $flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/flush_cli.py do_operate $type $flush_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $is_eva == "1" ]] && [[ $operate == "info" ]]
then
	echo python realtime/flush_cli.py front_info $type $flush_type --day $day --time_str $time_str --mode $mode
	python realtime/flush_cli.py front_info $type $flush_type --day $day --time_str $time_str --mode $mode

elif [[ $is_eva == "1" ]] && [[ $operate == "flush" ]]
then
	echo python realtime/flush_cli.py flush_front $type $flush_type --day $day --time_str $time_str --mode $mode
	python realtime/flush_cli.py flush_front $type $flush_type --day $day --time_str $time_str --mode $mode

elif [[ $flush_type =~ "pull_info" ]] || [[ $flush_type =~ "pullinfo" ]]
then
	echo python realtime/flush_cli.py pull_info $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/flush_cli.py pull_info $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $flush_type == "simple" ]]
then
	echo python realtime/flush_cli.py simple_flush $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/flush_cli.py simple_flush $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

else
	echo 不支持type:$type flush-type:$flush_type

fi

