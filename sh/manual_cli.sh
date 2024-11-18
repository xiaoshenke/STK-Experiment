#!/bin/bash

echo ATTENTION: MANUAL-CMDS CLI

day=#
time_str=#
mode='now'

type=''
ignore_cache=1

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
		fi
		declare -i now=$now+1
		;;
	esac
	shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

#is_code_types=$(python realtime/flush_cli.py is_code_types $type)
#is_eva=$(python realtime/flush_cli.py is_front_type $flush_type)

#elif [[ $is_code_types == "1" ]] && [[ $is_eva == "1" ]]
#then
#	echo 不支持code-types+eva类型 不过可以  sh/front_cli.sh $type $flush_type --mode $mode --day $day --time_str $time_str
#	exit 2

is_xls=$(python realtime/manual_cli.py is_xls $type)

if [[ $type =~ "pool" ]]
then
	echo python realtime/manual_cli.py pool $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/manual_cli.py pool $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $type == "codetypes" ]] || [[ $type == "code_types" ]] 
then
	echo python realtime/manual_cli.py code_types --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
        python realtime/manual_cli.py code_types --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $type == "market" ]]
then
	echo python realtime/manual_cli.py market --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/manual_cli.py market --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

elif [[ $is_xls == "1" ]]
then
	echo python realtime/manual_cli.py xls $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/manual_cli.py xls $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

else
	echo 当前不支持类型$type
fi

