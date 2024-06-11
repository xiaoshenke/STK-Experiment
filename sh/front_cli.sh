#!/bin/bash

echo ATTENTION: FRONT-CMDS CLI

day=#
time_str=#
mode=#

type=''
front_type=#
fronts=#
subs=#
back_type=#
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
	-back | --back)
                shift
                back_type=$1
                ;;
	-fronts | --fronts)
		shift
		fronts=$1
		;;
	-subs | --subs)
		shift
		subs=$1
		;;
	-ignore_cache | --ignore_cache)
                shift
                ignore_cache=$1
                ;;
        -help | --help)
		echo usage sh/realtime/flush_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] [--subs bbb] type
                exit 1
                ;;
        *)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		elif [ $now -eq 1 ]
		then
			front_type=$1
		elif [ $now -eq 2 ]
		then
			back_type=$1
		else
			fronts=$1
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
	front_type=$2
fi

if [ $# -eq 3 ]
then
	type=$1
	front_type=$2
	back_type=$3
fi

if [ $# -eq 3 ]
then
	type=$1
	front_type=$2
	back_type=$3
	fronts=$4
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

python realtime/flush_cli.py flush_front $type $front_type --day $day --time_str $time_str --mode $mode --back $back_type --fronts $fronts --subs $subs --ignore_cache $ignore_cache

