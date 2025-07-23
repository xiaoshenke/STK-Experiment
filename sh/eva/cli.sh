#!/bin/bash

echo ATTENTION: WRAP python eva/cli.py do_eva CLI

day=#
time_str=#
mode='now'

type=''
front_type=''
desc=#
back_type=#
fake=#
ignore_cache=1
debug=0
open=0
now=0
log=1
add=0
level=0
silent=0
open_jpg=1
do_report=1

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
	-silent | --silent)
		shift
		silent=$1
		;;
	-level | --level)
		shift
		level=$1
		;;
	-desc | --desc | --reason | -reason)
		shift
		desc=$1
		;;
	-log | --do_log | --log)
		shift
		log=$1
		;;
	-do_report | --do_report | --report)
		shift
		do_report=$1
		;;
	-add | --add_codes | --add)
		shift
		add=$1
		;;
	-open_jpg | --open_jpg)
		shift
		open_jpg=$1
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
		elif [ $now -eq 2 ]
		then
			desc=$1
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

echo python eva/cli.py do_eva --day $day --time_str $time_str --mode $mode $type $front_type --open 1 --do_log 1 [real] --open $open --do_log $log --ignore_cache $ignore_cache --back $back_type --debug $debug --do_report $do_report --open_jpg $open_jpg --add $add --desc $desc --level $level

python eva/cli.py do_eva --day $day --time_str $time_str --mode $mode $type $front_type --ignore_cache $ignore_cache --open $open --back $back_type --debug $debug --do_log $log --do_report $do_report --open_txt 1 --open_jpg $open_jpg --add $add --desc $desc --level $level --silent $silent
# --fake $fake
