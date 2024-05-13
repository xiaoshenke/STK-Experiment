#!/bin/bash

echo ATTENTION: FLUSH-CMDS CLI

day=#
time_str=#
mode=#

# 默认行情类型为zhendang
hq_type='zhendang'
type=''
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
		echo usage sh/hangqing_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] type
                exit 1
                ;;
        *)
		# set value to type|hq_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		else
			hq_type=$1
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
	hq_type=$2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

if [[ $hq_type == "zhendang" ]]
then
	echo python realtime/hangqing_cli.py zhendang $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py zhendang $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
elif [[ $hq_type == "maichong" ]]
then
	echo python realtime/hangqing_cli.py maichong $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
	python realtime/hangqing_cli.py maichong $type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache
else
	echo 输入的行情类型$hq_type 不正确
fi
