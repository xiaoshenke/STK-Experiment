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
	-fronts | --fronts)
		shift
		fronts=$1
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
		echo usage sh/front_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] type eva [fronts]
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
			fronts=$1
		else
			back_type=$1
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
	fronts=$3
fi

if [ $# -gt 3 ]
then
	type=$1
	front_type=$2
	fronts=$3
	back_type=$4
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

is_code_types=$(python realtime/flush_cli.py is_code_types "$type")

######## code-types branch logic
if [[ $is_code_types == "1" ]]
then
	echo ########## 为code-types类型
	echo python realtime/cts_cli.py front $type $front_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache

	python realtime/cts_cli.py front "$type" $front_type --day $day --time_str $time_str --mode $mode --ignore_cache $ignore_cache 
	exit 2
fi

if [[ $front_type == "simple" ]]
then
	echo python realtime/flush_cli.py flush $type --day $day --time_str $time_str --mode $mode --flush_type $front_type --ignore_cache $ignore_cache
	python realtime/flush_cli.py flush $type --day $day --time_str $time_str --mode $mode --flush_type $front_type --ignore_cache $ignore_cache
	exit 2
fi

####### flush front branch logic
echo python realtime/flush_cli.py flush_front $type $front_type --day $day --time_str $time_str --mode $mode --back $back_type --fronts $fronts --subs $subs --ignore_cache $ignore_cache --debug $debug

python realtime/flush_cli.py flush_front $type $front_type --day $day --time_str $time_str --mode $mode --back $back_type --fronts $fronts --subs $subs --ignore_cache $ignore_cache --debug $debug

