#!/bin/bash

echo ATTENTION: wrap realtime/buyer_plan_cli.py 

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

day=#
time_str=#
mode='now'
type=''
bp_type='default'
ignore_cache=1
debug=0
open=0
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
	-debug | --debug)
		shift
		debug=$1
		;;
	-ignore_cache | --ignore_cache)
		shift
		ignore_cache=$1
		;;
	-help | --help)
		#echo usage sh/eva_cli.sh [--day abc] [--time_str xyz] [--mode aaa ] type eva [fronts]
		python realtime/buyer_plan_cli.py help
		exit 1
		;;
        *)
		# set value to type|flush_type by now-flag
		if [ $now -eq 0 ]
		then
			type=$1
		elif [ $now -eq 1 ]
		then
			bp_type=$1
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
elif [[ -z $bp_type ]]
then
	echo bp_type empty.
	exit 2
fi

path=`pwd`
export PYTHONPATH=$path:$PYTHONPATH

is_list=$(python realtime/buyer_plan_cli.py is_list $type)
is_code_type=$(python realtime/buyer_plan_cli.py is_code_type $type)

if [[ $is_list == "1" ]]
then
	echo python realtime/buyer_plan_cli.py pool --day $day --time_str $time_str --mode $mode $type $bp_type
	python realtime/buyer_plan_cli.py pool --day $day --time_str $time_str --mode $mode $type $bp_type

elif [[ $type =~ "maichong" ]]
then
	echo python realtime/buyer_plan_cli.py maichong --day $day --time_str $time_str --mode $mode $type
	python realtime/buyer_plan_cli.py maichong --day $day --time_str $time_str --mode $mode $type

elif [[ $type == "lhgk" ]] || [[ $type == "lihao_gaokai" ]]
then
	echo python realtime/buyer_plan_cli.py lihao_gaokai --day $day --time_str $time_str --mode $mode 
	python realtime/buyer_plan_cli.py lihao_gaokai --day $day --time_str $time_str --mode $mode 

elif [[ $type =~ "baochong" ]]
then
	echo python realtime/buyer_plan_cli.py baochong --day $day --time_str $time_str --mode $mode 
	python realtime/buyer_plan_cli.py baochong --day $day --time_str $time_str --mode $mode 

elif [[ $type == "wenhe" ]]
then
	echo python realtime/buyer_plan_cli.py wenhe --day $day --time_str $time_str --mode $mode 
	python realtime/buyer_plan_cli.py wenhe --day $day --time_str $time_str --mode $mode 

elif [[ $type == "gwwhfq" ]] || [[ $type == "wenhe_tuichao" ]] || [[ $type == "whtc" ]] 
then
	echo python realtime/buyer_plan_cli.py gaowei_wenhe_fenqi --day $day --time_str $time_str --mode $mode 
	python realtime/buyer_plan_cli.py gaowei_wenhe_fenqi --day $day --time_str $time_str --mode $mode 

elif [[ $type == "yztl" ]] || [[ $type == "youzi_tuoli" ]] 
then
	echo python realtime/buyer_plan_cli.py youzi_tuoli --day $day --time_str $time_str --mode $mode 
	python realtime/buyer_plan_cli.py youzi_tuoli --day $day --time_str $time_str --mode $mode 

elif [[ $type == "yzzd" ]] || [[ $type == "youzi" ]] || [[ $type == "youzi_zhudao" ]] 
then
	echo python realtime/buyer_plan_cli.py youzi_zhudao --day $day --time_str $time_str --mode $mode 
	python realtime/buyer_plan_cli.py youzi_zhudao --day $day --time_str $time_str --mode $mode 

elif [[ $is_code_type == "1" ]]
then

	echo python realtime/buyer_plan_cli.py xls --day $day --time_str $time_str --mode $mode $type $bp_type
	python realtime/buyer_plan_cli.py xls --day $day --time_str $time_str --mode $mode $type $bp_type
else
	echo 当前不支持类型$type $bp_type
fi

