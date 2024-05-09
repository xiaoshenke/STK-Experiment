#!/bin/bash

echo ATTENTION: FLUSH-CMDS CLI

day=#
time_str=#
mode=#

type=''
flush_type='simple'
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
		else
			flush_type=$1
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

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python realtime/flush_cli.py flush $type --day $day --time_str $time_str --mode $mode --flush_type $flush_type --ignore_cache $ignore_cache
python realtime/flush_cli.py flush $type --day $day --time_str $time_str --mode $mode --flush_type $flush_type --ignore_cache $ignore_cache

