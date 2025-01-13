#!/bin/bash

echo ATTENTION: WRAP python eva/cli.py do_eva CLI

day=#
time_str=#
mode='now'

type=''
front_type=''
back_type=#
fake=#
ignore_cache=1
debug=0
open=0
now=0
log=1

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
	-fake | --fake)
		shift
		fake=$1
		;;
	-log | --log)
		shift
		log=$1
		;;
	-back | --back)
		shift
		back_type=$1
		;;
	-debug | --debug)
		shift
		debug=$1
		;;
	-open | --open)
		shift
		open=$1
                ;;
	-ignore_cache | --ignore_cache)
		shift
		ignore_cache=$1
		;;
	-help | --help)
		echo usage sh/eva_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] type eva [fronts]
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
		fi
		declare -i now=$now+1
                ;;
        esac
        shift
done

if [[ -z $type ]]
then
	echo type empty.
	exit 2
elif [[ -z $front_type ]]
then
	echo front_type empty.
	exit 2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

echo python eva/cli.py do_eva --day $day --time_str $time_str --mode $mode $type $front_type --open $open --back $back_type --debug $debug --fake $fake --do_log $log

python eva/cli.py do_eva --day $day --time_str $time_str --mode $mode $type $front_type --open $open --back $back_type --debug $debug --fake $fake --do_log $log
