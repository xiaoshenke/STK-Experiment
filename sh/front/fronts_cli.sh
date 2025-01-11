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
ignore_cache=1
open=0

# update 2024-12-17: flush->info
operate='info'
debug=0

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
	-open | --open)
		shift
		open=$1
		;;
	-fronts | --fronts)
		shift
		fronts=$1
		;;
	-front | --front | --front_type | -front_type | --eva | -eva)
		shift
		front_type=$1
		;;
	-subs | --subs)
		shift
		subs=$1
		;;
	-debug | --debug)
		shift
		debug=$1
		;;
	-ignore_cache | --ignore_cache)
		shift
		ignore_cache=$1
		;;
	-help | --help)
		echo usage sh/fronts_cli.sh code-type fronts-type [operate] [--front abc] [--day abc] [--time_str xyz] [--mode aaa ] 
		exit 1
		;;
        *)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		elif [ $now -eq 1 ]
		then
			fronts=$1
		elif [ $now -eq 2 ]
		then
			operate=$1
		fi
		declare -i now=$now+1
		;;
        esac
        shift
done

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

if [[ $operate == "info" ]]
then
	echo python realtime/fronts_cli.py info $type $fronts --day $day --time_str $time_str --mode $mode --front_type $front_type --ignore_cache $ignore_cache
	python realtime/fronts_cli.py info $type $fronts --day $day --time_str $time_str --mode $mode --front_type $front_type --ignore_cache $ignore_cache --do_log 1
	exit 2

elif [[ $operate == "flush" ]]
then
	echo python realtime/fronts_cli.py flush $type $fronts --day $day --time_str $time_str --mode $mode --front_type $front_type --ignore_cache $ignore_cache --open $open
	python realtime/fronts_cli.py flush $type $fronts --day $day --time_str $time_str --mode $mode --front_type $front_type --ignore_cache $ignore_cache --open $open --do_log 1

else
	echo sh/front/fronts_cli.sh not support operate:$operate

fi
